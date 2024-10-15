from odoo import models, fields

class DudoxxTask(models.Model):
    _name = 'dudoxx.task'
    _description = 'Dudoxx Automation Task'
    
    name = fields.Char(string="Task Name", required=True)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date")
    status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new')
