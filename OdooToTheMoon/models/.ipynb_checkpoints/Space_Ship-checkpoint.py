# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError 

class SpaceShip(models.Model):
    _name = 'space.spaceship'
    _description = 'space_spaceship'
    
    name = fields.Char(string="Nombre de la nave", required=True)
    qtyPassengers = fields.Integer(string="Cantidad de pasajeros")
    activeShip = fields.Boolean(string="Activa")
    height = fields.Float(string="Altura (m)")
    diameter = fields.Float(string="Diametro (m)")
    weight = fields.Float(string="Peso (T)")
    fuelType = fields.Selection(string="Tipo de combustible", 
                              selection=[('1','Hidrogeno liquido'),
                                        ('2','Combustible fosil'),
                                        ('3', 'Combustible solido')],
                               copy=False)
    shipType = fields.Selection(string="Tipo de nave", 
                              selection=[('1','Vehiculo Lanzadera'),
                                        ('2','Nave no tripulada'),
                                        ('3','Nave tripulada')],
                               copy=False)
    mission_ids = fields.One2many(space.mission,inverse_name='spaceship_id',string="Misiones asignadas")
    
    @api.constrains("height","diameter")
    def check_shipDimensions(self):
        record = self
        if record.height < 2*(record.diameter):
            raise UserError('El ancho de la nave no puede ser mayor que su altura')
    