# -*- coding: utf-8 -*-

from odoo import http


class SpaceApp(http.Controller):
    @http.route('/library/', auth='public', website=True)
    def index(self,**kw):
        available_books = http.request.env['library.book'].search([])
        return http.request.render('Library_Management.available_books_website',{
                'book':available_books,
        })
        