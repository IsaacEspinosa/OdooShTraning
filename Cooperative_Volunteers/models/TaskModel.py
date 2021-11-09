# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime, dateutil, pytz
from odoo.exceptions import UserError,ValidationError 

class TaskModel(models.Model):
    _name = 'volunteers.task'
    _description = 'Model for the tasks'
    
    name = fields.Char(string="Nombre de la tarea",required = True)
    taskDescription = fields.Text(string='Descripcion')
    startTime = fields.Datetime(string="Hora de inicio", default=datetime.datetime.today())
    endTime = fields.Datetime(string="Hora de fin")
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
                                copy=False,defult='1',readonly=True)
    leader = fields.Many2one(comodel_name="res.partner",string="Lider",required=True)
    volunteer = fields.Many2many(comodel_name="res.partner",string="Voluntario")#,compute="check_availability")
    
        
    @api.onchange("volunteer")
    def is_leader(self):
        for record in self.volunteer:
            if record.name == self.leader.name:
                raise UserError("El voluntario que intentas ingresar es el lider de la tarea")
            
    #@api.onchange("volunteer")
    #def check_availability(self):
    #    start_time = fields.Date.from_string(self.startTime)
    #    end_time = fields.Date.from_string(self.endTime)
    #    record_volunteer = self.volunteer.name
    #    b = self.volunteer.filtered(lambda c: c.name == record_volunteer)
    #    if len(b) != 0:
    #        for record in b:
    #            raise ValidationError("No puede ser %d")%(record)
    #            st = fields.Date.from_string(record.startTime)
    #            raise ValidationError("No puede ser")
    #            et = fields.Date.from_string(record.endTime)
    #            if not((st > start_time and st > end_time) or (et < start_time and et < endTime)):
    #                raise ValidationError("El voluntario se encuentra ocupado en el tiempo dado")
    
    @api.onchange("leader")
    def check_leader(self):
        record = self
        if record.leader != "" and record.stateTask == "1":
            record.stateTask = "2"
        if record.leader =="" and record.stateTask != "1":
            raise UserError("La tarea necesita un lider")