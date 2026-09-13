// Copyright (c) 2026, vishal and contributors
// For license information, please see license.txt

// frappe.query_reports["assignment-1"] = {
// 	filters: [
// 		// {
// 		// 	"fieldname": "my_filter",
// 		// 	"label": __("My Filter"),
// 		// 	"fieldtype": "Data",
// 		// 	"reqd": 1,
// 		// },
// 	],
// };

frappe.query_reports["Assignment"] = {
    filters: [
        {
            fieldname: "department",
            label: "Department",
            fieldtype: "Data"
        }
    ]
};