import frappe

def daily_maintenance():
    frappe.log_error(
        title="Scheduler Test",
        message="My daily scheduler is running"
    )