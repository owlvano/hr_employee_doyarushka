# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Employee(models.Model):

    _inherit = "hr.employee"

    first_work_day = fields.Date('First Work Day')
    days_limit = fields.Integer()
    days_since_first_work_day = fields.Integer('Days Since the First Work Day', compute='_calculate_days')


    @api.depends('first_work_day', 'days_limit')
    def _calculate_days(self):
    	return (datetime.today() - first_work_day).days

    @api.multi
    def _compute_newly_hired_employee(self):
        read_group_result = self.env['hr.applicant'].read_group(
            ['|',
             (self.days_limit, '=?',  self.days_since_first_work_day),
             (self.days_limit, '>',  self.days_since_first_work_day)
            ],
            ['emp_id'], ['emp_id'])
        result = dict((data['emp_id'], data['emp_id_count'] > 0) for data in read_group_result)
        for record in self:
            record.newly_hired_employee = result.get(record.id, False)
