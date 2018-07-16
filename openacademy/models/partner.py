# -*- coding: utf-8 -*-

from odoo import  models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    #  instructors
    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many(
        'openacademy.session',string="Attended Sessions",
        readonly=True)
    other_field =  fields.Boolean(default = True)
