
import frappe

@frappe.whitelist()
def calculate_bonus(employee):
    doc = frappe.get_doc("Employee", employee)

    return doc.salary * 0.10