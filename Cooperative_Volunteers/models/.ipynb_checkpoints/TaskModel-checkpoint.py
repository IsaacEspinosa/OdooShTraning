# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import datetime, dateutil, pytz
import math
from odoo.exceptions import UserError,ValidationError 

class TaskModel(models.Model):
    _name = 'volunteers.task'
    _description = 'volunteers_task'
    _rec_name = 'name'
    
    name = fields.Char(string="Nombre de la tarea",required = True)
    taskDescription = fields.Text(string='Descripcion')
    startTime = fields.Float(string="Hora de inicio", digits=(2,2))
    endTime = fields.Float(string="Hora de fin", digits=(2,2))
    startDate = fields.Date(string="Fecha de inicio")
    endDate = fields.Date(string="Fecha de fin")
    startDateTime = fields.Datetime(string="Fecha y hora de inicio",store=True)
    endDateTime = fields.Datetime(string="Fecha y hora de fin",store=True)
    todayDate = fields.Date(string='Today', default=lambda s: fields.Date.context_today(s))
    taskType = fields.Selection(string="Tipo de tarea",
                             selection=[('1','Recurrente'),
                                        ('2','Unica'),
                                        ],
                                copy=False,default='2')
    frecuency = fields.Selection(string="Frecuencia",
                             selection=[('1','Diario'),
                                        ('2','Semanal'),
                                        ('3','Mensual'),
                                        ],
                                copy=False)
    stateTask = fields.Selection(string="Estado",
                             selection=[('1','Borrador'),
                                        ('2','Lista'),
                                        ('3','En progreso'),
                                        ('4','Terminada'),
                                        ],
                                copy=False,default='1',readonly=True)
    leader_id = fields.Many2one(comodel_name="res.partner",string="Lider",required=True)
    volunteer_ids = fields.Many2many(comodel_name="res.partner",string="Voluntario")#,compute="check_availability")
    
    @api.onchange("volunteer_ids")
    def is_leader(self):
        for record in self.volunteer_ids:
            if record.name == self.leader_id.name:
                raise UserError("El voluntario que intentas ingresar es el lider de la tarea")
    
    @api.constrains("startTime","endTime")
    def check_time(self):
        if self.startTime > 23 or self.endTime > 23 or self.startTime < 0 or self.endTime < 0:
            raise UserError("Hora no valida")
        if self.startTime > self.endTime:
            raise UserError("La hora de fin no puede ser antes de la hora de inicio")
        
    @api.constrains("startDate","endDate")
    def check_Date(self):
        if self.startDate and self.endDate:
            if self.startDate > self.endDate:
                raise UserError("La fecha de fin no puede ser antes de la fecha de inicio")
            
    @api.constrains("leader_id")
    def check_leader(self):
        record = self
        if record.leader_id.name != "" and record.stateTask == "1":
            record.stateTask = "2"
        if record.leader_id.name == "" and record.stateTask != "1":
            raise UserError("La tarea necesita un lider")
    
    @api.constrains("startDate","endDate","startTime","endTime","todayDate")
    def _computeDateTime(self):
        for record in self:
            if record.startDate and record.endDate and record.startTime and record.endTime:
                if record.todayDate.strftime('%Y-%m-%d') <= record.endDate.strftime('%Y-%m-%d'):
                    sd = datetime.datetime.strftime(record.todayDate,'%Y-%m-%d')
                    parte_decimal1, parte_entera1 = math.modf(record.startTime)
                    parte_decimal2, parte_entera2 = math.modf(record.endTime)
                    parte_entera1 = str(int(parte_entera1))
                    parte_entera2 = str(int(parte_entera2))
                    parte_decimal1 = str(int(parte_decimal1 * 60))
                    parte_decimal2 = str(int(parte_decimal2 * 60))
                    if len(parte_entera1) == 1:
                           parte_entera1 = '0'+ parte_entera1
                    if len(parte_entera2) == 1:
                           parte_entera2 = '0'+ parte_entera2
                    if len(parte_decimal1) == 1:
                           parte_decimal1 = '0'+ parte_decimal1
                    if len(parte_decimal2) == 1:
                           parte_decimal2 = '0'+ parte_decimal2
                    record.startDateTime = datetime.datetime.strptime(sd + ' ' + parte_entera1 + ":" +
                                                                 parte_decimal1 + ":00",'%Y-%m-%d %H:%M:%S')
                    record.endDateTime = datetime.datetime.strptime(sd + ' ' + parte_entera2 + ":" +
                                                                 parte_decimal2+ ":00",'%Y-%m-%d %H:%M:%S')
                else:
                    record.startDateTime = ""
                    record.endDateTime = ""


    