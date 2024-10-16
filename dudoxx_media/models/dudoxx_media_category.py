from odoo import models, fields

class DudoxxMediaCategory(models.Model):
    _name = 'dudoxx.media.category'
    _description = 'Dudoxx Media Category'

    name = fields.Char(string='Name', required=True, index=True, unique=True)
    description = fields.Text(string='Description')