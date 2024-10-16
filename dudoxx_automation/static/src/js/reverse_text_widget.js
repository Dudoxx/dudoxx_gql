/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillUpdateProps } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

console.log("Loading ReverseTextWidget...");

export class ReverseTextWidget extends Component {
    setup() {
        console.log("Setting up ReverseTextWidget...");

        // Ensure 'data' is available and log it
        const originalText = this.props.data || '';
        console.log("Initial text loaded:", originalText);

        this.state = useState({
            reversedText: this.reverseText(originalText),
        });

        // Log the initial reversed text
        console.log("Initial reversed text:", this.state.reversedText);

        // Update reversed text when props.data changes
        onWillUpdateProps((nextProps) => {
            const updatedText = nextProps.data || '';
            console.log("Updated text from props:", updatedText);
            this.state.reversedText = this.reverseText(updatedText);
            console.log("Updated reversed text:", this.state.reversedText);
        });
    }

    reverseText(text) {
        console.log("Reversing text:", text);
        const reversed = text.split('').reverse().join('');
        console.log("Reversed result:", reversed);
        return reversed;
    }
}

// Define required props, including 'data'
ReverseTextWidget.props = {
    ...standardFieldProps,
    data: { type: String, optional: true, default: '' },
};

// Define the template for the widget
ReverseTextWidget.template = "dudoxx_automation.ReverseTextWidget";

// Registering the widget
registry.category("fields").add("reverse_text", ReverseTextWidget);

console.log("ReverseTextWidget registered in the registry.");
