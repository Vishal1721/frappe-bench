
import frappe
import time
from frappe.utils import now

@frappe.whitelist()
def get_default_amount(expense_type):
    default_amount = frappe.db.get_value('Expense Type',expense_type,'amount')
    return {
        "default_amount":default_amount
    }
@frappe.whitelist()
def get_employee_department(employee):
    department = frappe.db.get_value('Employee3',employee,'department')
    return {
        "department": department
    }


@frappe.whitelist()
def test():
    q = frappe.qb.get_query(
        "Asset Request",
        fields=[
            "name",
            "employee",
            "total_amount",
            {"items": ["asset", "quantity", "rate", "amount"]}
        ]
    )

    return q.run(as_dict=True)


@frappe.whitelist()
def click_method():
    return {
        "word":"hi i am vishal"
    }
@frappe.whitelist()
def send_chart_data(label, value):

    frappe.publish_realtime(
        "test_event",
        {
            "label": label,
            "points": [value]
        }
    )

    return "Data sent"

@frappe.whitelist()
def test_progress():

    print("🔥 FUNCTION STARTED")

    for i in range(0, 101, 10):

        print("🔥 PUBLISHING:", i)

        frappe.publish_progress(
            i,
            title="Processing",
            description=f"Progress: {i}%"
        )

        time.sleep(1)

    print("🔥 FUNCTION FINISHED")

    return "Completed"

@frappe.whitelist()
def generate_report():

    frappe.publish_progress(
        10,
        title="Generating Report",
        description="Collecting data..."
    )

    # do database work

    frappe.publish_progress(
        50,
        title="Generating Report",
        description="Processing data..."
    )

    # more work

    frappe.publish_progress(
        100,
        title="Generating Report",
        description="Report completed"
    )

    return "Done"
    
def sample():
    print("Hi")
@frappe.whitelist()
def send_realtime_message():
    frappe.publish_realtime(
        "student_update",
        message={
            "status":"Active",
            "message": "Hello from Frappe server!"
        }
    )

    return "Event published"

@frappe.whitelist()
def update_student_status(student_name):
    doc=frappe.get_doc("Student",student_name)
    doc.status="Inactive"
    doc.save(ignore_permissions=True)
    frappe.publish_realtime(
        "Student_update",
        message={"status":doc.status}
    )
    return "SucessFully changed"

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



