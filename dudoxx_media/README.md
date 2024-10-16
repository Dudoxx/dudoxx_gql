# Dudoxx Media Manager

## Overview

Dudoxx Media Manager is an Odoo 16 module designed to handle medical audio and image files with a modern, user-friendly UI. It provides functionality for storing, managing, and processing media files in a healthcare setting.

## Features

- Upload and manage audio and image files
- Categorize media files
- Tag-based organization
- Secure access control
- File integrity checks
- Workflow management (Draft, In Review, Published)
- Custom audio player widget

## Installation

1. Clone this repository into your Odoo addons directory:
   ```
   git clone https://github.com/dudoxx/dudoxx_media.git
   ```
2. Update your Odoo addons path to include the new module.
3. Restart your Odoo server.
4. Go to Apps and search for "Dudoxx Media Manager".
5. Click "Install" to activate the module.

## Configuration

After installation, you need to set up user access:

1. Go to Settings > Users & Companies > Users
2. Edit the users who need access to the media manager
3. Under "Access Rights", find the "Dudoxx Media Groups" section
4. Assign the appropriate role (User, Reviewer, or Admin)

## Usage

### Uploading Media Files

1. Navigate to Dudoxx Media > Media Files
2. Click "Create" to upload a new file
3. Fill in the required information and upload the file
4. Save the record

### Managing Categories and Tags

1. Go to Dudoxx Media > Categories or Dudoxx Media > Tags
2. Create, edit, or delete categories and tags as needed

### Reviewing and Publishing Files

1. Open a media file in draft status
2. Click "Submit for Review" to change its status
3. Reviewers can then "Approve" or "Reject" the file

## Development

### Adding New Features

1. Modify the models in `models/` directory
2. Update views in `views/dudoxx_media_views.xml`
3. Add any new security rules in `security/`
4. For frontend changes, modify `static/src/js/dudoxx_media_widgets.js` and `static/src/css/dudoxx_media.css`

### Running Tests

To run the unit tests:

```
./odoo-bin -i dudoxx_media -d your_database --test-enable
```

## Support

For any issues or feature requests, please create an issue on the GitHub repository.

## License

This project is licensed under LGPL-3. See LICENSE file for details.