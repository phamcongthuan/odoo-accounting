from odoo import models, fields, api


class Payment(models.Model):
    _name = 'teammate.salary.payment'
    _description = 'Salary payment'

    month_year = fields.Char(string='Month & Year')
    name = fields.Char(string='Name')
    position = fields.Char(string='Position')
    base_salary = fields.Float(string='Base salary')
    project_bonus = fields.Float(string='Project Bonus')
    tax = fields.Float(string='Tax')
    total = fields.Float(string='Total', compute='compute_total')
    date_paid = fields.Datetime(string='Date paid')

    @api.depends('base_salary', 'project_bonus', 'tax')
    def compute_total(self):
        for x in self:
            x.total = (x.base_salary + x.project_bonus) * (1 - x.tax)


