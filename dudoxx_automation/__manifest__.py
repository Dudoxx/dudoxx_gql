{
    "name": "Dudoxx Automation",
    "version": "1.0",
    "author": "Walid Boudabbous, DUDOXX UG",
    "category": "Automation",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "security/access_rules.xml",
        "views/main_menu.xml",
        "views/dudoxx_task_views.xml",
        "views/render_properties_widget_template.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "dudoxx_automation/static/src/css/dudoxx_automation.css",
            "dudoxx_automation/static/src/js/dudoxx_automation.js"
        ],
        "web.assets_backend": [
            "/dudoxx_automation/static/src/js/reverse_text_widget.js",
            "/dudoxx_automation/static/src/xml/reverse_text_widget_template.xml",
            "/dudoxx_automation/static/src/js/**/*",
            "/dudoxx_automation/static/src/xml/**/*",
            "dudoxx_automation/static/src/js/render_properties_widget.js"
        ]
    },
    "installable": True,
    "application": True
}
