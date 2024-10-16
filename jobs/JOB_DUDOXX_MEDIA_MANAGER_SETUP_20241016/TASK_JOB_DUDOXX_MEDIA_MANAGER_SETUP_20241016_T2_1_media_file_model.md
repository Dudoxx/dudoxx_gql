# Task 2.1: Define Media File Model

- Created the Media File Model (dudoxx.media.file) with the following fields:
  - name (Char): File name, required
  - file_type (Selection): File type (Audio, Image)
  - file_content (Binary): Media file content
  - file_size (Float): File size in MB, auto-calculated
  - created_date (Datetime): Date added
  - owner_id (Many2one): Reference to the owner (user)
  - status (Selection): File status (Draft, In Review, Published)
  - hash_code (Char): Unique file hash for integrity verification
