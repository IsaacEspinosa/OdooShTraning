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
                             selection=[('1','Recoger basura'),
                                        ('2','Ayuda comunitaria'),
                                        ('3','Pago voluntario'),
                                        ],
                                copy=False)
    repeat = fields.Boolean(string="Tarea usual", default=True)
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
    leader = fields.Text(string="Lider")
    
    @api.onchange("leader")
    def check_leader(self):
        record = self
        if record.leader != "" and record.stateTask == "1":
            record.stateTask = "2"
        if record.leader =="" and record.stateTask != "1":
            raise UserError("La tarea necesita un lider")