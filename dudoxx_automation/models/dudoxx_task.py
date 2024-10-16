from odoo import models, fields, api

class DudoxxTask(models.Model):
    _name = 'dudoxx.task'
    _description = 'Dudoxx Automation Task'
    
    # Basic task details
    name = fields.Char(string="Task Name", required=True)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date")
    status = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')],
        string="Status",
        default='new'
    )

    # Progress and priority fields
    countdown_field = fields.Integer(string="Countdown", default=10)
    progress = fields.Float(string="Progress", default=0.0)
    is_urgent = fields.Boolean(string="Is Urgent", default=False)
    priority_level = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string="Priority Level",
        default='medium'
    )
    completion_date = fields.Date(string="Completion Date")
    task_code = fields.Char(string="Task Code", size=12)

    # File handling fields
    file_data = fields.Binary(string="File Data", inverse="_set_file_name")
    file_name = fields.Char(string="File Name")  # Stores the name of the uploaded file

    # Text and document processing fields
    extracted_text = fields.Text(string="Extracted Text")
    cleaned_text = fields.Text(string="Cleaned Text")

    # Additional metadata fields
    file_type = fields.Selection(
        [('pdf', 'PDF'), ('image', 'Image'), ('text', 'Text')],
        string="File Type"
    )
    computation_time = fields.Float(string="Computation Time (s)")
    word_count = fields.Integer(string="Word Count")
    token_count = fields.Integer(string="Token Count")
    summary = fields.Html(string="Summary")

    @api.onchange("file_binary")
    def _onchange_file_binary(self):
        """Automatically set the task name to the filename if not already set."""
        for record in self:
            if record.file_name and not record.name:
                record.name = record.file_name

    def _set_file_name(self):
        """Sets the task name based on the uploaded file's filename if not already set."""
        for record in self:
            if record.file_name and not record.name:
                record.name = record.file_name
