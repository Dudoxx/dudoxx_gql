/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

export class CountdownWidget extends Component {
    setup() {
        this.state = useState({ countdown: 10, fontSize: 12 });

        const interval = setInterval(() => {
            if (this.state.countdown > 0) {
                this.state.countdown -= 1;
                this.state.fontSize += 2; // Increase font size
            } else {
                clearInterval(interval); // Stop countdown at 0
            }
        }, 1000); // Update every second
    }
}

CountdownWidget.template = "dudoxx_automation.CountdownWidget";

registry.category("fields").add("countdown_widget", CountdownWidget);
