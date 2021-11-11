# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError 

class CopyBook(models.Model):
    _name = "library.copybook"
    _description ="library_copybook"
    
    book_id = fields.Many2one(comodel_name="library.book",string="Existencias",ondelete="cascade")
    name = fields.Char(string="Nombre", related="book_id.name",readonly=True)
    ISBN = fields.Char(String="ISBN", related="book_id.ISBN",readonly=True)
    id = fields.Char(string="Identificador")
    rentals_ids = fields.Many2many(comodel_name="library.rental",string="Alquileres")
   
    
