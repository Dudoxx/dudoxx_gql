from odoo import models, fields, api, _
from odoo.exceptions import UserError

class DudoxxMediaFile(models.Model):
    _name = 'dudoxx.media.file'
    _description = 'Dudoxx Media File'

    # ... (existing fields and methods)

    def submit_for_review(self):
        """Submit a media file for review"""
        for record in self:
            if record.status == 'draft':
                record.status = 'in_review'
            else:
                raise UserError(_("Only draft media files can be submitted for review."))

    def approve(self):
        """Approve a media file"""
        for record in self:
            if record.status == 'in_review':
                record.status = 'published'
            else:
                raise UserError(_("Only media files in review can be approved."))

    def reject(self):
        """Reject a media file"""
        for record in self:
            if record.status == 'in_review':
                record.status = 'draft'
            else:
                raise UserError(_("Only media files in review can be rejected."))