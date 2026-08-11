# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

logger = frappe.logger("Employee4")
logger.setLevel("INFO")

class Employee1(Document):
    def validate(self):
        logger.info(
            f"Employee created: {self.name} by {frappe.session.user}"
        )
