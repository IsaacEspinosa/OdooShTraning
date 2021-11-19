# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError 
from datetime import date

class CopyBook(models.Model):
    _name = "library.copybook"
    _description ="library_copybook"
    
    book_id = fields.Many2one(comodel_name="library.book",string="Existencias",ondelete="cascade")
    name = fields.Char(string="Nombre", related="book_id.name",store=True)
    ISBN = fields.Char(String="ISBN", related="book_id.ISBN",store=True)
    copybook_id = fields.Char(string="Identificador",size=10)
    rentals_ids = fields.Many2many(comodel_name="library.rental",string="Alquileres")
    available_copybook = fields.Boolean(string="Disponibilidad",default=True)
    today_check = fields.Date(string="Fecha de ultima comprobacion de disponibilidad")
    
    
                
   
    
