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
        frappe.msgprint("hi")
    def before_insert(self):
        frappe.msgprint("naa dha before_insert")
    def before_validate(self):
        frappe.msgprint("naa dha before_validate")
    def before_save(self):
        frappe.msgprint("naa dha before_save")
    def on_update(self):
        frappe.msgprint("naa dha on_update")
    def on_change(self):
        frappe.msgprint("naa dha on_change")
    
    def on_submit(self):
        frappe.msgprint("naa dha on_submit")
    def before_submit(self):
        frappe.msgprint("naa dha before_submit")
    def on_cancel(self):
        frappe.msgprint("naa dha on_cancel")
    def before_cancel(self):
        frappe.msgprint("naa dha before_cancel")
    def on_update_after_submit(self):
        frappe.msgprint("naa dha on_update_after_submit")
    def before_update_after_submit(self):
        frappe.msgprint("naa dha before_update_after_submit") 
    def after_delete(self):
         frappe.msgprint("naa dha after_delete") 
    def on_trash(self):
         frappe.msgprint("naa dha on_trash")
    def database_delete(self):
         frappe.msgprint("naa dha database_delete")