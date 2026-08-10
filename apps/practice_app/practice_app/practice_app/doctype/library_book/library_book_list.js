let count = 0;
frappe.listview_settings["Library Book"] = {
    add_fields:["book_title","author","status","self_number"],
     filters: [
        ["status", "=", "Lost"]
    ],
};