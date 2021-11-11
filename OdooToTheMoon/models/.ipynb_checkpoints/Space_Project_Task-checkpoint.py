# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = "project.task"
    
    mission_id = fields.Many2one(comodel_name="space.mission", string="Mision relacionada", ondelete='cascade',required=True)