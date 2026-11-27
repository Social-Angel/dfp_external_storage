"""A web link saved as a File stays a plain link (no upload, no error).

Run: bench --site <site> run-tests --module dfp_external_storage.dfp_external_storage.doctype.dfp_external_storage.test_web_links --skip-before-tests
"""

import frappe
from frappe.tests import IntegrationTestCase


class TestWebLinks(IntegrationTestCase):
	def test_web_link_file_saves_as_a_link(self):
		f = frappe.get_doc({"doctype": "File", "file_url": "https://example.org/logo.png", "is_private": 0}).insert(ignore_permissions=True)
		self.assertEqual(f.file_url, "https://example.org/logo.png")
		self.assertFalse(f.get("dfp_external_storage_s3_key"))
