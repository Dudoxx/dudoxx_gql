# Dudoxx Media Manager

The Dudoxx Media Manager is an Odoo 16 module designed to handle medical audio and image files with a modern, user-friendly UI. It provides features for storing, managing, and processing media files in a healthcare setting, including media uploading, categorization, and secure access.

## Installation

1. Clone the `dudoxx_media` repository to your Odoo addons directory.
2. Install the module through the Odoo UI or by running `odoo -u dudoxx_media` in your terminal.

## Configuration

1. Create the necessary user groups:
   - Dudoxx Media Admin
   - Dudoxx Media User
   - Dudoxx Media Reviewer
2. Assign users to the appropriate groups based on their roles and permissions.
3. (Optional) Customize the CSS styles in `static/src/css/dudoxx_media.css` to match your branding and design preferences.

## Usage

1. Navigate to the Media Files menu in your Odoo application.
2. Upload media files by clicking the "Create" button and filling out the required information.
3. Categorize files by assigning them to a media category.
4. Add relevant tags to media files for improved search and filtering.
5. Review and approve media files as needed, based on your user group permissions.

## Development

### Models
- `dudoxx.media.file`: Main model for managing media files.
- `dudoxx.media.category`: Model for categorizing media files.
- `dudoxx.media.tag`: Model for assigning tags to media files.

### Views
- Form View: Provides a user-friendly interface for managing media file details, including upload, categorization, and metadata.
- Tree View: Displays a compact list of media files.
- Kanban View: Groups media files by category with drag-and-drop support.

### Widgets
- `ImagePreviewWidget`: Displays a preview of image files in the form view.
- `AudioPlayerWidget`: Provides an inline audio player for medical audio files in the form view.

### Security
- User groups: Dudoxx Media Admin, Dudoxx Media User, Dudoxx Media Reviewer
- Access rules: Enforce permissions based on user groups and file ownership/status.

### Testing
- Unit tests for model methods, access control, and UI components.

### DevOps
- Continuous Integration (CI) and Continuous Deployment (CD) setup.
- Code linting and formatting checks.
- Test coverage reporting.

For more detailed information, please refer to the individual task documentation in the `JOB_DUDOXX_MEDIA_MANAGER_SETUP_20241016` folder.