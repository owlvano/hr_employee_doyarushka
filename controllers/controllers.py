# -*- coding: utf-8 -*-
from odoo import http

# class HrEmployeeDoyarushka(http.Controller):
#     @http.route('/hr_employee_doyarushka/hr_employee_doyarushka/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee_doyarushka/hr_employee_doyarushka/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee_doyarushka.listing', {
#             'root': '/hr_employee_doyarushka/hr_employee_doyarushka',
#             'objects': http.request.env['hr_employee_doyarushka.hr_employee_doyarushka'].search([]),
#         })

#     @http.route('/hr_employee_doyarushka/hr_employee_doyarushka/objects/<model("hr_employee_doyarushka.hr_employee_doyarushka"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee_doyarushka.object', {
#             'object': obj
#         })