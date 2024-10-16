# Dudoxx Attachment Module

This module provides a way to manage attachments within Odoo, including a comprehensive document workflow.

## Features

* Create, Read, Update, and Delete attachments.
* Track attachment name, file name, creation date, owner, and status.
* Store file data and content type.
* Unique hash code for each attachment.
* Role-based access control with granular permissions.
* Kanban, Tree, and Form views for easy management.
* Public and private API endpoints for integration.
* Hash processing and checksum validation.
* Custom CSS and JavaScript for enhanced backend UI styling.
* **Document Workflow:** Manage the lifecycle of attachments through different statuses.

## Security Groups

* **Dudoxx Attachment Admin:** Full access (read, write, create, delete).
* **Dudoxx Attachment User:** Limited to read access.
* **Dudoxx Attachment Editor:** Read and write access, can submit documents for review.
* **Dudoxx Attachment Reviewer:** Can approve or reject documents.

## Installation

1. Place the `dudoxx_attachment` module directory inside your Odoo addons directory.
2. In Odoo, go to Apps and update the app list.
3. Search for "Dudoxx Attachment" and install the module.

## Usage

### Views

* **Kanban View:** Displays attachments grouped by status.
* **Tree View:** Lists attachments with key information, including workflow status.
* **Form View:** Allows creating and editing attachments, including hash processing actions. Uses custom CSS classes for improved styling and layout.  Includes buttons for workflow transitions.

### CRUD Operations

The module exposes API endpoints for managing attachments:

* `/dudoxx_attachment/get`: Retrieve attachments (public).
* `/dudoxx_attachment/create`: Create a new attachment (user).
* `/dudoxx_attachment/update/{id}`: Update an existing attachment (user).
* `/dudoxx_attachment/delete/{id}`: Delete an attachment (user).

### Hash Processing

The form view provides actions for managing attachment hashes:

* **Compute Hash Code:** Automatically computes a SHA256 hash of the file data upon upload.
* **Update Checksum:**  Manually triggers a recalculation and update of the hash code.  Useful for verifying file integrity.  Uses custom JavaScript for interactivity.

## Custom Styling

This module includes custom CSS and JavaScript to enhance the backend UI:

* **CSS:**  Provides styles for form sections, buttons, and grid layouts, prefixed with `ddx_attachment_`.  See `static/src/css/ddx_attachment_styles.css` for details.
* **JavaScript:** Adds interactivity to form elements, such as the "Recalculate Hash" button.  See `static/src/js/ddx_attachment_script.js` for details.

## Permissions and Access


* Access levels are defined by security groups, ensuring fine-grained control over attachment management and workflow transitions.
* Record rules can be implemented to further restrict visibility based on specific criteria.


## Contributing

Contributions are welcome! Please submit pull requests or report issues on GitHub.

## Workflow Information

Attachments follow a defined workflow with the following statuses:

* **Draft:** Initial status when an attachment is created.
* **Pending Review:**  Submitted for review by an editor.
* **Reviewed:** Approved by a reviewer.
* **Rejected:** Rejected by a reviewer.
* **Finalized:** The final status, indicating completion of the workflow.

Users with appropriate permissions can transition attachments between these statuses using buttons in the form view.
