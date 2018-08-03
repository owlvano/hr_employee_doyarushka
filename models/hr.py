# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):

    _inherit = "hr.employee"

    first_work_day = fields.Date('First Work Day')
