import frappe


def after_build():
    raise RuntimeError("HOOK SUCCESS: practice_app after_build fired!")