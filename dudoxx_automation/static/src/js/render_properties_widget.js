/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RenderPropertiesWidget extends Component {
    setup() {
        // Define state to store record properties
        this.state = useState({ properties: {} });

        // Fetch properties on start
        onWillStart(async () => {
            const recordProps = await this.fetchRecordProperties();
            this.state.properties = recordProps;
        });
    }

    async fetchRecordProperties() {
        // Mocked fetch for properties
        const props = this.props.recordData || {};
        return props;
    }
}

RenderPropertiesWidget.props = {
    ...standardFieldProps,
    recordData: Object,
};

RenderPropertiesWidget.template = "dudoxx_automation.RenderPropertiesWidget";

// Registering the widget
registry.category("fields").add("render_properties", RenderPropertiesWidget);
