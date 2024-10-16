TASK 1: Define Workflow Status Field in dudoxx.attachment Model

Added the 'status' field to the dudoxx.attachment model to track document workflow stages. The field includes the following statuses: 'Draft', 'Pending Review', 'Reviewed', 'Rejected', and 'Finalized'. The tracking=True attribute is set to track changes in the status field.
