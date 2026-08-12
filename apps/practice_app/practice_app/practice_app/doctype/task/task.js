// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Task", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Task', {
	onload(frm) {
	    let dialog =new frappe.ui.Dialog({
	        title:"Task Subject",
	        fields:[
	            {"label":"Task Subject",
	            "fieldtype":"Data",
	            "fieldname" : "task_subject",
	            "reqd":1
	            }
	            ],
	            primary_action_label:"Create Task",
	            primary_action(values) {
	                frappe.call({
	                        method: "practice_app.api.task",
	                        args: {
	                            task_subject:values.task_subject
	                        },
	                        callback(r) {
	                            dialog.hide()
	                            frappe.msgprint({
                                title: "Success",
                                indicator: "green",
                                message:"Task created successfully."
                                });
	                        }
	                    })
	            }
	            
	    })
	    dialog.show()
	}
})
