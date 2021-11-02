# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime, dateutil, pytz

class TaskModel(models.Model):
    _name = 'volunteers.task'
    _description = 'Model for the tasks'
    
    taskName = fields.Char(string="Nombre de la tarea",required = True)
    taskDescription = fields.Text(string='Descripcion')
    startTime = fields.Date(string="Hora de inicio", default=datetime.datetime.today())
    endTime = fields.Date(string="Hora de fin")
    taskType = fields.Selection(string="Tipo de tarea",
                             selection=[('1','Recoger basura'),
                                        ('2','Ayuda comunitaria'),
                                        ('3','Pago voluntario'),
                                        ],
                             copy=False)
    repeat = fields.Boolean(string="Tarea usual", default=True)
    frecuency = fields.Integer(string="Frecuencia")
    
    