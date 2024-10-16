from odoo import models, fields

class DudoxxMediaCategory(models.Model):
    _name = 'dudoxx.media.category'
    _description = 'Dudoxx Media Category'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    
    media_file_ids = fields.One2many('dudoxx.media.file', 'category_id', string='Media Files')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Category name already exists !"),
    ]