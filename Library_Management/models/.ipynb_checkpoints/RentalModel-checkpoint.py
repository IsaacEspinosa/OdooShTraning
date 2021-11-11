from odoo import models, fields, api
import datetime, dateutil, pytz
from odoo.exceptions import UserError,ValidationError 

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'library_rental'
    
    customer_id = fields.Many2one(comodel_name="res.partner",string="Clientes",ondelete='cascade',required=True)
    name = fields.Char(string="Cliente",related='customer_id.name')
    books_ids = fields.Many2many(comodel_name="library.copybook",string="Libros rentados")
    loan_date = fields.Date(string="Fecha de prestamo", default=datetime.date.today())
    return_date = fields.Date(string="Fecha de devolucion")