from odoo import models, fields, api
import hashlib

class DudoxxAttachment(models.Model):
    _name = 'dudoxx.attachment'
    _description = 'Dudoxx Attachment Model'

    name = fields.Char(string='Name', required=True)
    file_name = fields.Char(string="File Name", required=False)
    creation_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
    owner = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.user)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending_review', 'Pending Review'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
        ('finalized', 'Finalized')
    ], string='Status', default='draft', tracking=True)
    content_type = fields.Char(string='Content Type')
    file_data = fields.Binary(string='File Data')
    hash_code = fields.Char(string='Hash Code', compute='compute_hash_code', store=True)

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        if 'status' in fields_list and defaults.get('status') is None:
            defaults['status'] = 'draft'
        return defaults


    @api.depends('file_data')
    def compute_hash_code(self):
        for record in self:
            if record.file_data:
                record.hash_code = hashlib.sha256(record.file_data).hexdigest()
            else:
                record.hash_code = False

    def submit_for_review(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'pending_review'

    def approve_review(self):
        for record in self:
            if record.status == 'pending_review':
                record.status = 'reviewed'

    def reject_review(self):
        for record in self:
            if record.status == 'pending_review':
                record.status = 'rejected'

    def finalize_document(self):
        for record in self:
            if record.status == 'reviewed':
                record.status = 'finalized'

    def back_to_draft(self):
        for record in self:
            record.status = 'draft'

    def back_to_pending_review(self):
        for record in self:
            if record.status in ('reviewed', 'finalized'):
                record.status = 'pending_review'

    def back_to_review(self):
        for record in self:
            if record.status == 'finalized':
                record.status = 'reviewed'

    def set_to_rejected(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'rejected'


    def update_checksum(self):
        for record in self:
            if record.file_data:
                record.hash_code = hashlib.sha256(record.file_data).hexdigest()
