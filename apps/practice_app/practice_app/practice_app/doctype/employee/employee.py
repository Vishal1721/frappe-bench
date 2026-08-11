# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

logger = frappe.logger("Employee")
logger.setLevel("INFO")

class Employee(Document):

    def background_test(self):
        print("Background method running")
        print("Employee:", self.name)

    def validate(self):
        logger.info(
            f"Employee created: {self.name} by {frappe.session.user}"
        )

    # def on_update(self):
    #     logger.info(
    #         f"Employee modified: {self.name} by {frappe.session.user}"
    #     )

    # def on_trash(self):
    #     logger.info(
    #         f"Employee deleted: {self.name} by {frappe.session.user}"
    #     )