# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Employee(models.Model):

    _inherit = "hr.employee"

    first_work_day = fields.Date('First Work Day')
    days_since_first_work_day = fields.Integer('Days Since the First Work Day', compute='_calculate_days')

    @api.depends('first_work_day')
    def _calculate_days(self):
        for record in self:
            if record.first_work_day:
                record.days_since_first_work_day = (datetime.now() - datetime.strptime(record.first_work_day, "%Y-%m-%d")).days

    @api.multi
    def _compute_newly_hired_employee(self):
        for record in self:         
                record.newly_hired_employee = (record.first_work_day == False or self.env['ir.values'].get_default('hr.employee.settings', 'days_limit') > record.days_since_first_work_day)

    @api.multi
    def _search_newly_hired_employee(self, operator, value):
        recs = self.search([]).filtered(lambda x : x.newly_hired_employee is True)
        if recs:
            return [('id', 'in', [x.id for x in recs])]
