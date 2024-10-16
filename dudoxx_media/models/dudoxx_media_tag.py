from odoo import models, fields

class DudoxxMediaTag(models.Model):
    _name = 'dudoxx.media.tag'
    _description = 'Dudoxx Media Tag'

    name = fields.Char(string='Name', required=True)
    
    media_file_ids = fields.Many2many('dudoxx.media.file', string='Media Files')