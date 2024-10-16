from odoo import http
from odoo.http import request

class DudoxxAttachmentController(http.Controller):

    @http.route('/dudoxx_attachment/get', type='json', auth='public')
    def get_attachments(self):
        attachments = request.env['dudoxx.attachment'].search([])
        return attachments.read(['name', 'creation_date', 'owner', 'status'])


    @http.route('/dudoxx_attachment/create', type='json', auth='user')
    def create_attachment(self, **kw):
        request.env['dudoxx.attachment'].create(kw)
        return {'status': 'success'}


    @http.route('/dudoxx_attachment/update/<int:attachment_id>', type='json', auth='user')
    def update_attachment(self, attachment_id, **kw):
        attachment = request.env['dudoxx.attachment'].browse(attachment_id)
        if attachment.exists():
            attachment.write(kw)
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Attachment not found'}


    @http.route('/dudoxx_attachment/delete/<int:attachment_id>', type='json', auth='user')
    def delete_attachment(self, attachment_id):
        attachment = request.env['dudoxx.attachment'].browse(attachment_id)
        if attachment.exists():
            attachment.unlink()
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Attachment not found'}
