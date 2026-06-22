from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")
