from odoo import models, fields


class Member(models.Model):
    _name = 'teammate.member'
    _description = 'Member'

    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    birth = fields.Datetime(string='Birth')
    position = fields.Char(string='Position')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
