# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeSettings(models.TransientModel):

    _name = "hr.employee.settings"
    _inherit = 'res.config.settings'

    days_limit = fields.Integer(string = "Days' Limit of a New Employee")

    # -----Days' Limit of a New Employee-----

    @api.multi
    def get_default_new_employee_days_limit(self, fields):
        return {'days_limit': self.env['ir.values'].get_default('hr.employee.settings', 'days_limit')}

    @api.multi
    def set_default_new_employee_days_limit(self):
        for record in self:
            self.env['ir.values'].set_default('hr.employee.settings', 'days_limit', record.days_limit)