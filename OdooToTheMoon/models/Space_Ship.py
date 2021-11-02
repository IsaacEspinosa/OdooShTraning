# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SpaceShip(models.Model):
    _name = 'space.spaceship'
    _description = 'Model for the rocket'
    
    shipDimensions = fields.Float(string="Dimensiones del barco")
    fuelType = fields.Selection(string="Tipo de combustible", 
                              selection=[('1','Magna'),
                                        ('2','Premium'),
                                        ('3', 'Diesel')],
                               copy=False)
    shipType = fields.Selection(string="Tipo de nave", 
                              selection=[('1','Grande'),
                                        ('2','Mediana'),
                                        ('3','Pequeña')],
                               copy=False)
    active = fields.Boolean(string="Activa", store = True)
    
    