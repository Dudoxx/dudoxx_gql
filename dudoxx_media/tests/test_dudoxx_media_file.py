from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestDudoxxMediaFile(TransactionCase):

    def setUp(self):
        super(TestDudoxxMediaFile, self).setUp()
        self.MediaFile = self.env['dudoxx.media.file']
        self.test_file = self.MediaFile.create({
            'name': 'Test File',
            'file_type': 'image',
            'file_path': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==',  # 1x1 pixel base64 encoded
        })

    def test_file_creation(self):
        self.assertTrue(self.test_file.id)
        self.assertEqual(self.test_file.name, 'Test File')
        self.assertEqual(self.test_file.file_type, 'image')

    def test_file_size_computation(self):
        self.assertTrue(self.test_file.file_size > 0)

    def test_hash_code_generation(self):
        self.assertTrue(self.test_file.hash_code)

    def test_file_size_constraint(self):
        with self.assertRaises(ValidationError):
            self.MediaFile.create({
                'name': 'Large File',
                'file_type': 'image',
                'file_path': 'a' * (501 * 1024 * 1024),  # 501 MB file
            })

    def test_workflow_transitions(self):
        self.assertEqual(self.test_file.status, 'draft')
        self.test_file.submit_for_review()
        self.assertEqual(self.test_file.status, 'in_review')
        self.test_file.approve()
        self.assertEqual(self.test_file.status, 'published')
        self.test_file.reject()
        self.assertEqual(self.test_file.status, 'draft')

    def test_integrity_check(self):
        self.assertTrue(self.test_file.check_integrity())
        self.test_file.file_path = 'modified_content'
        self.assertFalse(self.test_file.check_integrity())