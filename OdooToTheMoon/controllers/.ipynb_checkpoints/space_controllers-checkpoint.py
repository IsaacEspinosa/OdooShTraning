# -*- coding: utf-8 -*-

from odoo import http


class SpaceApp(http.Controller):
    @http.route('/spaceapp/', auth='public', website=True)
    def index(self,**kw):
        mission = http.request.env['space.mission'].search([])
        return http.request.render('OdooToTheMoon.mission_website',{
                'mission':mission,
        })
        