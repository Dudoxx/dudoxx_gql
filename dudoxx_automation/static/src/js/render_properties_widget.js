/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart, onWillUpdateProps, onPatched } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class RenderPropertiesWidget extends Component {
    setup() {
        this.state = useState({ properties: {}, labels: {}, types: {} });

        // Initial data fetching on component start
        onWillStart(async () => {
            await this.updateRecordProperties();
        });

        // Update properties whenever external changes occur in record data
        onWillUpdateProps(async (nextProps) => {
            if (nextProps.record.data !== this.props.record.data) {
                await this.updateRecordProperties(nextProps.record.data);
            }
        });

        // Re-fetch and re-render properties after each DOM patch
        onPatched(async () => {
            await this.updateRecordProperties();
        });
    }

    async updateRecordProperties(recordData = this.props.record.data) {
        const recordProps = await this.fetchRecordProperties(recordData);
        this.state.properties = { ...recordProps.properties };  // Ensuring reactivity with spread operator
        this.state.labels = { ...recordProps.labels };
        this.state.types = { ...recordProps.types };
    }

    async fetchRecordProperties(recordData) {
        const properties = {};
        const labels = {};
        const types = {};

        for (const [key, value] of Object.entries(recordData || {})) {
            if (key !== "id" && key !== "__last_update") {
                properties[key] = key === "countdown" ? Math.floor(value) : value; // Only keep whole seconds for countdown

                const field = this.props.record.fields[key];
                if (field) {
                    labels[key] = field.string;
                    types[key] = field.type;
                } else {
                    labels[key] = key;
                    types[key] = "string";
                }
            }
        }

        return { properties, labels, types };
    }

    formatValue(key, value) {
        const fieldType = this.state.types[key];
        if (key === "countdown_field") {
            return Math.floor(value); // Displays only the whole seconds
        } else if (fieldType === "boolean") {
            return value ? "Yes" : "No";
        } else if (fieldType === "date" || fieldType === "datetime") {
            return new Date(value).toLocaleDateString();
        } else if (fieldType === "text") {
            return value ? value.replace(/\n/g, "<br>") : "";
        }
        return value;
    }

    getClassForType(key) {
        const fieldType = this.state.types[key];
        return fieldType === "boolean" ? "field-boolean"
             : fieldType === "date" || fieldType === "datetime" ? "field-date"
             : fieldType === "text" ? "field-text"
             : "field-default";
    }
}

RenderPropertiesWidget.props = {
    ...standardFieldProps,
    record: Object,
};

RenderPropertiesWidget.template = "dudoxx_automation.RenderPropertiesWidget";
registry.category("fields").add("render_properties", RenderPropertiesWidget);
