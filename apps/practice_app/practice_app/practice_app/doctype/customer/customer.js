// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
	refresh(frm) {
        frm.add_custom_button('send_email',()=>{
            frappe.msgprint("Email send successfully")
        })
	},
});
