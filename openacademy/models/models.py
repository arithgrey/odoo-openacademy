# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

def get_uid(self , *a ):
     return  self.env.uid

class Course(models.Model):
     _name = 'openacademy.course'

     name = fields.Char(string='Title', required=True)
     start_date = fields.Date(default = fields.Datetime.now)
     description = fields.Text()
     responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True ,
                                      default = get_uid )
     session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")


class Session(models.Model):
     _name = 'openacademy.session'

     name = fields.Char(required=True)
     start_date =fields.Date()
     duration = fields.Float(digits=(6, 2), help="Duration in days")
     seats = fields.Integer(string="Number of seats")
     instructor_id = fields.Many2one('res.partner', string="Instructor" ,
                                     domain=['|', ('instructor', '=', True),
                                             ('category_id.name', 'ilike', "Teacher")])

     course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
     attendee_ids = fields.Many2many('res.partner', string="Attendees")

     taken_seats = fields.Float(string = "Taken seats" , compute='_taken_seats')
     active = fields.Boolean(default=True)
     @api.depends('seats', 'attendee_ids')
     def _taken_seats(self):
          #import  pdb; pdb.set_trace()
          for z in self:
               if not z.seats:
                    z.taken_seats = 0.0
               else:
                    z.taken_seats = 100.0 * len(z.attendee_ids) / z.seats
















