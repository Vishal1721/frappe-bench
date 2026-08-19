
import frappe
import time
from frappe.utils import now

#Assignment: js-frappecall Assignment
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

#Assignment: python-api-utilities Assignment
@frappe.whitelist()
def get_recent_record():
    results = frappe.get_list("ToDo",fields=["name","description","owner"],
    order_by="creation desc",limit=5)
    for row in results:
        value=frappe.db.get_value("User",row["owner"],"email")
        row["email"]=value
    current_time=now()

    return {
        "timestamps":current_time,
        "records":results
    }
@frappe.whitelist()
def create_document(values):
    value = frappe._dict(frappe.parse_json(values))
    doc=frappe.new_doc("Employee")
    doc.name1=value.employee_name
    doc.salary=value.salary
    doc.email=value.email

    doc.insert()
    frappe.db.commit()
    return doc.name

@frappe.whitelist(methods=["PATCH"])
def update_document(name,values):
    value = frappe._dict(frappe.parse_json(values))
    doc=frappe.get_doc("Employee",name)
    for field, new_value in value.items():
        doc.set(field, new_value)

    doc.save()
    frappe.db.commit()
    return doc.name

@frappe.whitelist()
def get_document():
    data = frappe.get_list("Employee",fields=["name","salary"])
    return data

# @frappe.whitelist(allow_guest=True, methods=["POST"])
# def delete_document(name):
#     frappe.log_error("....")
#     frappe.delete_doc("Employee",name,ignore_permissions=True)
#     frappe.db.commit()
#     return "success"

@frappe.whitelist()
def delete_document(name):
    print("NAME RECEIVED:", name)

    frappe.delete_doc(
        "Employee",
        name
    )

    frappe.db.commit()

    return "success"

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



