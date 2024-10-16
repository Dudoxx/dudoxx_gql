# Task 3: Update Odoo Manifest File

**Task ID:** TASK_JOB_DUDOXX_ATTACHMENT_UI_STYLING_20241015_T3

**Description:** Modified `__manifest__.py` to include the new CSS and JavaScript files in the backend assets.

**File:** `dudoxx_attachment/__manifest__.py`

**Update Made:**

```python
"assets": {
    "web.assets_backend": [
        "dudoxx_attachment/static/src/css/ddx_attachment_styles.css",
        "dudoxx_attachment/static/src/js/ddx_attachment_script.js"
    ],
}
```

**Result:** Successfully updated the manifest file.
