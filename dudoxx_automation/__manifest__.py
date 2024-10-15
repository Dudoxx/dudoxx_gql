{
    "name": "Dudoxx Automation",
    "version": "1.0",
    "author": "Walid Boudabbous, DUDOXX UG",
    "category": "Automation",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "security/access_rules.xml",
        "views/main_menu.xml",
        "views/dudoxx_task_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "dudoxx_automation/static/src/css/dudoxx_automation.css",
            "dudoxx_automation/static/src/js/dudoxx_automation.js",
        ],
    },
    "installable": True,
    "application": True,
}
