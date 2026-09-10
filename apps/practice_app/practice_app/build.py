import frappe


def after_build():
    print("Hi")
    # raise RuntimeError("HOOK SUCCESS: practice_app after_build fired!")