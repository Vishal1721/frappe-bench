// frappe.listview_settings["Student"] = {
//     add_fields: ["student_name", "email"],

//     filters: [
//         ["email", "is", "set"]
//     ],
//      hide_name_column: true,
//     hide_name_filter: true,
//     onload(listview) {
//         console.log("Student List Loaded");
//     },
//     get_indicator(doc) {
//         if (doc.status === "Active") {
//             return ["Active", "green", "status,=,Active"];
//         }

//         return ["Inactive", "red", "status,=,Inactive"];
//     },
//     primary_action() {
//         console.log("Primary action clicked");
//         frappe.msgprint("Student primary action clicked");
//     },
//      get_form_link(doc) {
//         console.log("Current Student:", doc);

//         return `/app/student/${doc.name}`;
//     },
//      button: {
//         show(doc) {
//             return true;
//         },

//         get_label() {
//             return "View";
//         },

//         get_description(doc) {
//             return `View ${doc.student_name}`;
//         },

//         action(doc) {
//             frappe.set_route("Form", "Student", doc.name);
//         },

//     }

// };
frappe.listview_settings["Student"] = {
    dropdown_button: {
        get_label() {
            return "Actions";
        },

        buttons: [
            {
                get_label() {
                    return "View";
                },

                show(doc) {
                    return true;
                },

                get_description(doc) {
                    return `View ${doc.student_name}`;
                },

                action(doc) {
                    frappe.set_route("Form", "Student", doc.name);
                }
            },

            {
                get_label() {
                    return "Show Name";
                },

                show(doc) {
                    return true;
                },

                get_description(doc) {
                    return `Show ${doc.student_name}`;
                },

                action(doc) {
                    frappe.msgprint(
                        `Student: ${doc.student_name}`
                    );
                }
            }
        ]
    }
};