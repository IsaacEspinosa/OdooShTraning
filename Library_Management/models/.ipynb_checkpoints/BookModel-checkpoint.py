# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError 
from datetime import date

class Book(models.Model):
    _name = 'library.book'
    _description = 'library_book'
    
    name = fields.Char(string="Libro",required=True,store=True)
    author = fields.Char(string="Autor",required=True)
    editors = fields.Text(string="Editores")
    publisher = fields.Char(string="Editorial")
    editionYear = fields.Integer(string="Año de edicion")
    gender = fields.Selection(string="Genero",
                             selection=[('1','Cientifico'),
                                        ('2','Literatura y lingüísticos'),
                                        ('3','Poéticos'),
                                        ('4','De referencia o consulta'),
                                        ('5','Juveniles'),
                                        ('6','Ficción'),
                                        ('7','Recreativos'),
                                        ],
                             copy=False)
    noteText = fields.Text(string="Texto de nota")
    ISBN = fields.Char(string="ISBN",required=True,size=17,default=" ",store=True)
    copybook_ids = fields.One2many(comodel_name="library.copybook",inverse_name='book_id',string="Existencias")
    
    @api.onchange("ISBN")
    def check_ISBN_lenght(self):
        for record in self:
            if len(record.ISBN.replace("-", "")) == 13 or record.ISBN == " ":
                if record.ISBN != " ":
                    a = record.ISBN.replace("-", "")
                    record.ISBN = a[0:3] + "-" + a[3:5] + "-" + a[5:7] + "-" + a[7:12] + "-" + a[12]
                else:
                    record.ISBN = ""
            else:
                raise UserError("El ISBN debe de contener 13 caracteres")
                
    def button_availability(self):
        self = self.sudo()
        for record in self:
            for item in record.copybook_ids:
                if item.rentals_ids:
                    for rental in item.rentals_ids:
                        if rental.loan_date <= date.today() <= rental.return_date:
                            item.available_copybook=False
                        else:
                            item.available_copybook=True
                else:
                    item.available_copybook=True
                item.today_check = date.today()
        return True