from odoo import models, fields

class DudoxxMediaTag(models.Model):
    _name = "dudoxx.media.tag"
    _description = "Media Tag"

    name = fields.Char(string="Name", required=True)
