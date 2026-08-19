// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contact1", {
	setup(frm) {
        let d = new frappe.ui.Dialog({
            title: 'Enter Customer Details',
            fields:
            [
            {
            label: 'First Name',
            fieldname: 'first_name',
            fieldtype: 'Data',
            reqd: 1
            }
        ],
        primary_action_label:"Submit",
        primary_action(values) {
            frappe.route_options={
                first_name:values.first_name
            }
            d.hide()
            frappe.new_doc("Employee")
        }
        })
        d.show()
	},
});

