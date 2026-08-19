import frappe


def before_install():
    print(">>> BEFORE INSTALL")


def after_install():
    print(">>> AFTER INSTALL")


def after_sync():
    print(">>> AFTER SYNC")