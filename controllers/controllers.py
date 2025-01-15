# -*- coding: utf-8 -*-
# from odoo import http


# class Cesta(http.Controller):
#     @http.route('/cesta/cesta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cesta/cesta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cesta.listing', {
#             'root': '/cesta/cesta',
#             'objects': http.request.env['cesta.cesta'].search([]),
#         })

#     @http.route('/cesta/cesta/objects/<model("cesta.cesta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cesta.object', {
#             'object': obj
#         })
