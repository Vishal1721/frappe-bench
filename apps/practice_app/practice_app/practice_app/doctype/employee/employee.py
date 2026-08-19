# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now

logger = frappe.logger("Employee",allow_site=False)
logger.setLevel("INFO")

class Employee(Document):

    def background_test(self):
        print("Background method running")
        print("Employee:", self.name)

    def validate(self):
        logger.info(
            f"Employee created: {self.name} by {frappe.session.user}"
        )
    def before_save(self):
        self.joining_date=now()
    def on_update(self):
        logger.warning(
            f"Employee modified: {self.name} by {frappe.session.user}"
        )

    def on_trash(self):
        logger.critical(
            f"Employee deleted: {self.name} by {frappe.session.user}"
        )
    