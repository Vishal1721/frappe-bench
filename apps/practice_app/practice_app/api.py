
import frappe
import time

@frappe.whitelist()
def task(task_subject):
    doc=frappe.new_doc("Task")
    doc.task_subject=task_subject
    doc.insert()
    return doc.name
    
# @frappe.whitelist()
# def demo_progress():
#     for i in range(10):
#         frappe.publish_progress(
#             (i + 1) * 10,
#             title="Import",
#             description=f"Processing {i+1}/10"
#         )
#         time.sleep(1)

#     return "Done"


# @frappe.whitelist()
# def start_short_job():
#     frappe.enqueue(
#     "practice_app.api.generate_pdf",
#     queue="short"
# )

#     return "Short job enqueued"


# def generate_pdf():
#     print("Short job")


# @frappe.whitelist()
# def start_long_job():
#     frappe.enqueue(
#         "practice_app.api.long_job",
#         queue="long"
#     )

#     return "Long job enqueued"



