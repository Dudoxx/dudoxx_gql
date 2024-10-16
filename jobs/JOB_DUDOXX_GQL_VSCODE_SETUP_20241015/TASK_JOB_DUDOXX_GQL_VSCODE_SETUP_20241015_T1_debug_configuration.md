# Task 1: Configure VS Code Debugging

## Description
Set up `launch.json` for debugging with `debugpy`.

## Configuration
The following configuration was added to `launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Dudoxx Debug",
            "type": "python",
            "request": "launch",
            "program": "/Users/optron/dev/projects/odoo-boiler/odoo/odoo-bin",
            "args": [
                "-c",
                "${workspaceFolder}/dudoxx.conf",
                "-u",
                "dudoxx_form",
                "--dev",
                "xml"
            ],
            "env": {
                "PYTHONPATH": "/Users/optron/dev/projects/odoo-boiler/odoo"
            },
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "${workspaceFolder}",
            "python": "/Users/optron/miniconda3/envs/dudoxx-mvp/bin/python"
        }
    ]
}
```

## Outcome
The VS Code debugging configuration is set up for the Dudoxx GQL project.
