# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Model to store information abaut the books'
    
    name = fields.Char(string="Libro")
    author = fields.Char(string="Autor")
    editors = fields.Text(string="Editores")
    publisher = fields.Char(string="Editorial")
    editionYear = fields.Integer(string="Año de edicion")
    gender = fields.Selection(string="Genero",
                             selection=[('1','Terror'),
                                        ('2','comedia'),
                                        ('3','Historia'),
                                        ('4','Niños')
                                        ],
                             copy=False)
    
    