# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError 


class SpaceMission(models.Model):
    _name='space.mission'
    _description = 'space_mission'
    
    spaceship_id = fields.Many2one(comodel_name="space.spaceship", string='Nave espacial', ondelete='restrict',required=True)
    tripulation_ids = fields.Many2many(comodel_name="res.partner",string="Tripulacion")
    name = fields.Char(sting="Nombre de la mision")
    launch_date = fields.Date(string="Fecha de lanzamiento")
    return_date = fields.Date(string="Fecha de regreso")
    project_ids = fields.One2many(comodel_name="project.task",inverse_name="mission_id", string="Proyectos")
    
    