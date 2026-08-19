import frappe


def before_write(file_size=None):
    frappe.logger("file_test").info(
        f"BEFORE WRITE FILE HOOK CALLED, size={file_size}"
    )
def delete_file():
    raise RuntimeError("HOOK SUCCESS: practice_app before_write fired!")