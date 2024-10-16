TASK 2: Implement Workflow Transition Methods

Implemented methods for workflow transitions in the dudoxx.attachment model. The following methods were added:

- submit_for_review(): Changes status from 'Draft' to 'Pending Review'.
- approve_review(): Changes status from 'Pending Review' to 'Reviewed'.
- reject_review(): Changes status from 'Pending Review' to 'Rejected'.
- finalize_document(): Changes status from 'Reviewed' to 'Finalized'.
