// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
//     onload(frm) {
//         // Only add the row automatically if the document is brand new and empty
//         if (frm.is_new() && (!frm.doc.courses || frm.doc.courses.length === 0)) {
//             let row = frm.add_child("courses", {
//                 course: "Python",
//                 credit: 4 // Match the 'credits' field from your backend JSON
//             });
//             frm.refresh_field("courses");
//         }
//     }
// });

// frappe.ui.form.on("Student Course", {
//     form_render(frm, cdt, cdn) {
//         console.log("Child row opened as form");
//         console.log("CDT:", cdt);
//         console.log("CDN:", cdn);
//     }
// });
// frappe.ui.form.on("Student", {
//     refresh(frm) {
//         frm.add_custom_button("Selected Courses", () => {
//             let selected = frm.get_selected();

//             console.log(selected);
//         });
//     }
// });
// frappe.ui.form.on("Student", {
//     refresh(frm) {
//         frm.add_custom_button("Email Student", () => {
//             frm.email_doc();
//         });
//     }
// })
// frappe.ui.form.on("Student", {
//     refresh(frm) {
//         frm.set_intro(
//             "Please complete the Student details",
//             "blue"
//         );
//     }
// });
// frappe.ui.form.on("Student", {
//     refresh(frm) {
//         if (!frm.doc.email) {
//             frm.disable_save();
//         }
//     }
// });
// frappe.ui.form.on("Student", {
//     refresh(frm) {
//         let wrapper = frm.fields_dict.student_name.$wrapper;

//         frappe.ui.form.make_control({
//             parent: wrapper,
//             df: {
//                 label: "Due Date",
//                 fieldname: "due_date",
//                 fieldtype: "Date",
//                 change : function(value) {
//                     console.log(value.due_date)
//                 }
//               },

            
//             render_input: true
//         });
//     }
// });