# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo411(http.Controller):
#     @http.route('/odoo411/odoo411/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo411/odoo411/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo411.listing', {
#             'root': '/odoo411/odoo411',
#             'objects': http.request.env['odoo411.odoo411'].search([]),
#         })

#     @http.route('/odoo411/odoo411/objects/<model("odoo411.odoo411"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo411.object', {
#             'object': obj
#         })
