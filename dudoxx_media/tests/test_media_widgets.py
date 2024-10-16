import unittest
from odoo.tests.common import TransactionCase
from odoo.addons.dudoxx_media.static.src.js.dudoxx_media_widgets import ImagePreviewWidget, AudioPlayerWidget

class TestDudoxxMediaWidgets(TransactionCase):
    def setUp(self):
        super(TestDudoxxMediaWidgets, self).setUp()
        self.media_file = self.env['dudoxx.media.file'].create({
            'name': 'Test File',
            'file_type': 'image',
            'file_path': b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==',
        })

    def test_image_preview_widget(self):
        widget = ImagePreviewWidget(self.env, self.media_file)
        widget.willStart()
        self.assertEqual(widget.file_path, self.media_file.file_path)

    def test_audio_player_widget(self):
        widget = AudioPlayerWidget(self.env, self.media_file)
        widget.willStart()
        self.assertEqual(widget.file_path, self.media_file.file_path)