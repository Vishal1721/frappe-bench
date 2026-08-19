// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Employee", {
    // refresh(frm) {
    //     console.log("Student form refreshed");
    //     console.log(frm);
    //     console.log(frm.doc);
    //     console.log(frm.doc.status)
     setup(frm) {
        frm.set_query("department", () => {
            return {
                filters: {
                    status: "Active"
                }
            };
        });
    }
    // setup(frm) {
    //     frm.set_df_property("salary", "reqd", 1);
    // },
//     // refresh(frm) {
//     //     frm.set_df_property("salary", "reqd", 0);
//     // }
});