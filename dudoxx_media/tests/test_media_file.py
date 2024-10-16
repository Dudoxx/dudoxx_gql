import unittest
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

class TestDudoxxMediaFile(TransactionCase):
    def setUp(self):
        super(TestDudoxxMediaFile, self).setUp()
        self.media_file = self.env['dudoxx.media.file'].create({
            'name': 'Test File',
            'file_type': 'image',
            'file_path': b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==',
            'hash_code': '1234567890abcdef',
        })

    def test_generate_hash(self):
        hash_code = self.media_file.generate_hash(self.media_file.file_path)
        self.assertEqual(hash_code, '1234567890abcdef')

    def test_check_integrity_valid(self):
        self.assertTrue(self.media_file.check_integrity())

    def test_check_integrity_invalid(self):
        self.media_file.hash_code = '0123456789abcdef'
        self.assertFalse(self.media_file.check_integrity())

    def test_submit_for_review(self):
        self.media_file.submit_for_review()
        self.assertEqual(self.media_file.status, 'in_review')

    def test_submit_for_review_not_draft(self):
        self.media_file.status = 'in_review'
        with self.assertRaises(UserError):
            self.media_file.submit_for_review()

    def test_approve(self):
        self.media_file.status = 'in_review'
        self.media_file.approve()
        self.assertEqual(self.media_file.status, 'published')

    def test_approve_not_in_review(self):
        self.media_file.status = 'draft'
        with self.assertRaises(UserError):
            self.media_file.approve()

    def test_reject(self):
        self.media_file.status = 'in_review'
        self.media_file.reject()
        self.assertEqual(self.media_file.status, 'draft')

    def test_reject_not_in_review(self):
        self.media_file.status = 'published'
        with self.assertRaises(UserError):
            self.media_file.reject()

    def test_file_size_constraint(self):
        self.media_file.file_path = b'x' * (500 * 1024 * 1024 + 1)
        with self.assertRaises(ValidationError):
            self.media_file.save()