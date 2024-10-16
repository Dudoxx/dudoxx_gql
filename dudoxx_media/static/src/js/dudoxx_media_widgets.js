odoo.define('dudoxx_media.widgets', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ViewRegistry = require('web.view_registry');

    var _t = core._t;

    var ImagePreviewWidget = core.Widget.extend({
        template: 'dudoxx_media.ImagePreviewWidget',
        xmlDependencies: ['/dudoxx_media/static/src/xml/dudoxx_media_widgets.xml'],

        init: function (parent, record) {
            this._super(parent);
            this.record = record;
        },

        willStart: function () {
            var self = this;
            return this._super().then(function () {
                return rpc.query({
                    model: 'dudoxx.media.file',
                    method: 'read',
                    args: [[self.record.id], ['file_path']],
                }).then(function (data) {
                    self.file_path = data[0].file_path;
                });
            });
        },

        start: function () {
            this.$el.find('img').attr('src', 'data:image/*;base64,' + this.file_path);
        }
    });

    var AudioPlayerWidget = core.Widget.extend({
        template: 'dudoxx_media.AudioPlayerWidget',
        xmlDependencies: ['/dudoxx_media/static/src/xml/dudoxx_media_widgets.xml'],

        init: function (parent, record) {
            this._super(parent);
            this.record = record;
        },

        willStart: function () {
            var self = this;
            return this._super().then(function () {
                return rpc.query({
                    model: 'dudoxx.media.file',
                    method: 'read',
                    args: [[self.record.id], ['file_path']],
                }).then(function (data) {
                    self.file_path = data[0].file_path;
                });
            });
        },

        start: function () {
            this.$el.find('audio').attr('src', 'data:audio/*;base64,' + this.file_path);
        }
    });

    ViewRegistry.add('image_preview', ImagePreviewWidget);
    ViewRegistry.add('audio_player', AudioPlayerWidget);
});