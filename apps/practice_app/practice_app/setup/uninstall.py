import frappe

def after_uninstall():
    frappe.logger("uninstall_test").info(
        "practice_app was uninstalled"
    )