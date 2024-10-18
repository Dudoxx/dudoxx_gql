from odoo import models, fields

class DudoxxTaskAudio(models.Model):
    _inherit = 'dudoxx.task'

    audio_data = fields.Binary(string="Audio Data", attachment=True, help="Binary data of the recorded audio")
    audio_filename = fields.Char(string="Audio Filename", help="Name of the audio file")