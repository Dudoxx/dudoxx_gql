from odoo import models, fields

class DudoxxMediaCategory(models.Model):
    _name = "dudoxx.media.category"
    _description = "Media Category"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
