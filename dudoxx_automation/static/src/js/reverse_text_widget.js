/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillUpdateProps } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

console.log("Loading ReverseTextWidget...");

export class ReverseTextWidget extends Component {
    setup() {
        console.log("Setting up ReverseTextWidget...");

        // Initialize state with reversed text
        const originalText = this.props.value || '';
        console.log("Initial text loaded:", originalText);

        this.state = useState({
            reversedText: this.reverseText(originalText),
        });

        // Log the initial reversed text
        console.log("Initial reversed text:", this.state.reversedText);

        // Update reversed text when props.value changes
        onWillUpdateProps((nextProps) => {
            const updatedText = nextProps.value || '';
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

// Standard props to ensure compatibility
ReverseTextWidget.props = {
    ...standardFieldProps,
};

// Define the template for the widget
ReverseTextWidget.template = "dudoxx_automation.ReverseTextWidget";

// Registering the widget
registry.category("fields").add("reverse_text", ReverseTextWidget);

console.log("ReverseTextWidget registered in the registry.");
