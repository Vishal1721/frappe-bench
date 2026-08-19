frappe.pages['employee_form'].on_page_load = function (wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Employee Form',
        single_column: true
    });

    $(wrapper).find('.layout-main-section').html(`
        <div class="employee-form">
            <h3>Employee Details</h3>

            <div class="form-group">
                <label>Employee Name</label>
                <input
                    type="text"
                    id="employee_name"
                    class="form-control"
                    placeholder="Enter employee name"
                >
            </div>

            <div class="form-group">
                <label>Email</label>
                <input
                    type="email"
                    id="email"
                    class="form-control"
                    placeholder="Enter email"
                >
            </div>
			<div class="form-group">
                <label>Salary</label>
                <input
                    type="text"
                    id="Salary"
                    class="form-control"
                    placeholder="Enter salary"
                >
            </div>
            <button id="save_employee" class="btn btn-primary">
                Save Employee
            </button>
			 <button id="update_employee" class="btn btn-secondary">
                Update
            </button>

            <button id="delete_employee" class="btn btn-danger">
                Delete
            </button>
        </div>
    `);

    $('#save_employee').on('click', function () {
        console.log("Save clicked");

        const data = {
            employee_name: $('#employee_name').val(),
            email: $('#email').val(),
            department: $('#department').val()
        };
		frappe.call({
			method :"practice_app.api.create_document",
			args : {
				values:data
			},
			callback: (r)=> {
				console.log("successfully created",r)
			}
	})

        console.log("Employee data:", data);
    });
	$('#update_employee').on('click', function () {

    let dialog = new frappe.ui.Dialog({
        title: 'Update Employee',
        fields: [
            {
                label: 'Employee Name / ID',
                fieldname: 'name',
                fieldtype: 'Data',
                reqd: 1
            },
            {
                label: 'New Employee Name',
                fieldname: 'name1',
                fieldtype: 'Data'
            },
            {
                label: 'New Email',
                fieldname: 'email',
                fieldtype: 'Data'
            },
        ],
        primary_action_label: 'Update',

        primary_action(values) {

            console.log("Update data:", values);

            fetch("/api/method/practice_app.api.update_document", {
				method: "PATCH",
				headers: {
					"Content-Type": "application/json",
					"X-Frappe-CSRF-Token": frappe.csrf_token
				},
				body: JSON.stringify({
					name: values.name,
					values: values
				})
			})
			.then(response => response.json())
			.then(r => {
				console.log("UPDATE RESPONSE:", r);
			});
        }
    });

    dialog.show();
});

// ---

	$('#delete_employee').on('click', function () {

    let dialog = new frappe.ui.Dialog({
        title: 'Delete Employee',
        fields: [
            {
                label: 'Employee Name / ID',
                fieldname: 'name1',
                fieldtype: 'Data',
                reqd: 1
            }
        ],

        primary_action_label: 'Delete',

        primary_action(values) {
            console.log("Delete values:", values);

            frappe.call({
                method: "practice_app.api.delete_document",
                args: {
                    name: values.name1
                },
                callback: (r) => {
                    console.log("RESPONSE:", r);

                    if (r.exc) {
                        console.error("DELETE FAILED:", r.exc);
                        return;
                    }

                    console.log("DELETE SUCCESS:", r.message);
                    dialog.hide();
                }
            });
        }
    });

    dialog.show();
});

}