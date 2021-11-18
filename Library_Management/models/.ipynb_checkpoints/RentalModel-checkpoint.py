from odoo import models, fields, api
import datetime, dateutil, pytz
from odoo.exceptions import UserError,ValidationError 
from datetime import date

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'library_rental'
    
    customer_id = fields.Many2one(comodel_name="res.partner",string="Clientes",ondelete='cascade',required=True)
    name = fields.Char(string="Cliente",related='customer_id.name')
    books_ids = fields.Many2many(comodel_name="library.copybook",string="Libros rentados")
    loan_date = fields.Date(string="Fecha de prestamo", default=datetime.date.today())
    return_date = fields.Date(string="Fecha de devolucion")
    
    @api.onchange('books_ids')
    def check_availability(self):
        for record in self.books_ids:
            last_book = record[len(record)-1]
            if record.available_copybook == False and not record != last_book:
                   raise UserError("El libro que intentas alquilar no se encuentra disponible")
            if record.today_check != date.today():
                raise UserError("No se ha comprobado la disponibilidad de las existencias")
            record.available_copybook = False
    
    @api.constrains("loan_date","return_date")
    def check_Date(self):
        if self.loan_date and self.return_date:
            if self.loan_date > self.return_date:
                raise UserError("La fecha de devolucion no puede ser antes de la fecha del prestamo")
    
    @api.constrains("books_ids")
    def check_rentals(self):
        for record in self:
            if len(record.books_ids) == 0:
                raise UserError("El alquiler debe de contener al menos un libro")