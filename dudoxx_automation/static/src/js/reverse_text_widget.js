// static/src/js/reverse_text_widget.js
odoo.define('dudoxx_automation.ReverseTextWidget', function (require) {
    "use strict";
    
    const AbstractField = require('web.AbstractField');
    const fieldRegistry = require('web.field_registry');

    const ReverseTextWidget = AbstractField.extend({
        _render: function () {
            const originalText = this.value || '';
            const reversedText = originalText.split('').reverse().join('');
            this.$el.text(reversedText);
        },
    });

    fieldRegistry.add('reverse_text', ReverseTextWidget);

    return ReverseTextWidget;
});
