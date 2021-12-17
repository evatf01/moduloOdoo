# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo411(models.Model):
#     _name = 'odoo411.odoo411'
#     _description = 'odoo411.odoo411'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields


class Musica(models.Model):
    _name = "odoo411.musica"
    _description = 'odoo411.musica'
    name = fields.Char(string='Clave', required=True)
    grupo = fields.Char(string='Nombre del grupo', required=True)
    album = fields.Char(string='Nombre del album', required=True)
    


