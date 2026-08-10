# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee(Document):
    def background_test(self):
        print("Background method running")
        print("Employee:", self.name)