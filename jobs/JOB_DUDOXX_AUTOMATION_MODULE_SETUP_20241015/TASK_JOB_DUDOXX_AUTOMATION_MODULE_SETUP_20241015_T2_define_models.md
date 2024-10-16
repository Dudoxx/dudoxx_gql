# Task 2: Define Models

## Description
Create model definitions in the `models/` directory for the `dudoxx_automation` module.

## Steps Taken
1. Defined models in `models/` for core functionalities, including an example model `dudoxx_task`:
   ```python
   from odoo import models, fields

   class DudoxxTask(models.Model):
       _name = 'dudoxx.task'
       _description = 'Dudoxx Automation Task'
       
       name = fields.Char(string="Task Name", required=True)
       description = fields.Text(string="Description")
       due_date = fields.Date(string="Due Date")
       status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new')
   ```

## Outcome
The model `dudoxx.task` is defined with the necessary fields for the automation tasks.
