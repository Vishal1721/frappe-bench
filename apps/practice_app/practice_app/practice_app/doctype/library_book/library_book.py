# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

logger = frappe.logger("Library",allow_site=False)
logger.setLevel("INFO")
class LibraryBook(Document):
	def validate(self):
		logger.info(
            f"Book created: {self.name} by {frappe.session.user}"
        )
