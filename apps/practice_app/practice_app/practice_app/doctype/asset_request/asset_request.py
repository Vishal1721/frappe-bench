# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AssetRequest(Document):
    def before_validate(self):
        for row in self.items:
            if row.quantity<=0:
                frappe.throw(f"Quantity can't be zero")
            if row.rate<=0:
                frappe.throw(f"Rate can't be zero")
    def validate(self):
        self.validate_asset_quantity()

    def validate_asset_quantity(self):

        for row in self.items:
            if not row.asset or not row.quantity:
                continue
            
            available_quantity=frappe.db.get_value('Asset',row.asset,['available_quantity'])

            if row.quantity>available_quantity :
                frappe.throw(f"Not enough stock available.<br>"
                f"Available quantity: {available_quantity}")
            
    def before_save(self):
        total = 0
        for row in self.items:
            total = total + (row.quantity*row.rate)
        if total<=0:
            frappe.throw("Asset Request must contain at least one item.") 
        self.total_amount = total
        if total<100000:
            self.requires_approval= 0
        else:
            self.requires_approval = 1

    @frappe.whitelist()
    def get_employee_department(name):
        department = frappe.db.get_value('Employee',name,["department"])

        return department
        