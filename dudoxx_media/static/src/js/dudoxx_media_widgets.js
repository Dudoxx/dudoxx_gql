odoo.define('dudoxx_media.widgets', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var core = require('web.core');
var registry = require('web.field_registry');

var DudoxxAudioPlayer = AbstractField.extend({
    template: 'DudoxxAudioPlayer',
    events: {
        'click .play-pause': '_onPlayPause',
    },

    init: function () {
        this._super.apply(this, arguments);
        this.audio = new Audio();
    },

    _render: function () {
        this.$el.html(core.qweb.render('DudoxxAudioPlayer', {
            url: this.value,
        }));
        this.audio.src = this.value;
    },

    _onPlayPause: function () {
        if (this.audio.paused) {
            this.audio.play();
            this.$('.play-pause').text('Pause');
        } else {
            this.audio.pause();
            this.$('.play-pause').text('Play');
        }
    },
});

registry.add('dudoxx_audio_player', DudoxxAudioPlayer);

});