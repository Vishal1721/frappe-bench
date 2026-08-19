// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Book", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Employee", {
    // refresh(frm) {
    //     console.log("Student form refreshed");
    //     console.log(frm);
    //     console.log(frm.doc);
    //     console.log(frm.doc.status)
    email(frm) {
        if (frm.doc.email) {
            console.log("email entered",frm.doc.email);
        }
    }
});
