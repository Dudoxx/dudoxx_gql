from odoo import models, fields

class DudoxxMediaFile(models.Model):
    _name = "dudoxx.media.file"
    _description = "Media File"

    name = fields.Char(string="Name", required=True)
    file_type = fields.Selection([
        ("audio", "Audio"),
        ("image", "Image")
    ], string="File Type")
    file_content = fields.Binary(string="File Content")
    file_size = fields.Float(string="File Size (MB)", compute="_compute_file_size")
    created_date = fields.Datetime(string="Created Date", default=fields.Datetime.now)
    owner_id = fields.Many2one("res.users", string="Owner")
    status = fields.Selection([
        ("draft", "Draft"),
        ("in_review", "In Review"),
        ("published", "Published")
    ], string="Status", default="draft")
    hash_code = fields.Char(string="Hash Code", compute="_compute_hash_code")

    def _compute_file_size(self):
        # TODO: Implement file size calculation
        pass

    def _compute_hash_code(self):
        # TODO: Implement hash code generation
        pass
