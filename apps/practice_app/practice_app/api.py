
import frappe
import time

@frappe.whitelist()
def task(task_subject):
    doc=frappe.new_doc("Task")
    doc.task_subject=task_subject
    doc.insert()
    return doc.name
# Assignment: python-api-documentation Assignment    
@frappe.whitelist()
def query_generator():
    Employee = frappe.qb.DocType("Employee")
    Department = frappe.qb.DocType("Department")
    query = (
        frappe.qb
        .from_(Employee)
        .inner_join(Department)
        .on(Employee.department == Department.name)
        .select(
            Employee.name,
            Employee.salary,
            Department.department_name,
            Employee.joining_date
        )
    )
    results = query.run(as_dict=True)
    if results:
        doc = frappe.get_doc("Employee", results[0]["name"])
        doc.salary = 10000
        doc.save()
        frappe.db.commit()
    for row in results:
        frappe.db.set_value(
        "Employee",
        row["name"],
        "salary",
        10000
    )
    return results

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



