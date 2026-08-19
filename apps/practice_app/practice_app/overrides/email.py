import frappe


def get_sender_details():
    frappe.logger("email_test").info(
        "get_sender_details hook called"
    )

    return "Practice App", "noreply@example.com"