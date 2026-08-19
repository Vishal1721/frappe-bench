import frappe

import frappe

def execute():
    # 1. Use has_column to cleanly check if the column exists in the database table
    if not frappe.db.has_column("Employee", "migration_test_field"):
        
        # 2. Programmatically generate a secure Custom Field DocType definition
        custom_field = frappe.new_doc("Custom Field")
        custom_field.dt = "Employee"                      # Target DocType
        custom_field.fieldname = "migration_test_field"   # System column name
        custom_field.label = "Migration Test Field"       # UI Label
        custom_field.fieldtype = "Data"                   # Field structure type
        custom_field.insert(ignore_permissions=True)       # Save securely
        
        frappe.db.commit()
