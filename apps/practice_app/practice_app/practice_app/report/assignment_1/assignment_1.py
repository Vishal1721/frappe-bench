# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

from frappe import _


def execute(filters: dict | None = None):
    """Return columns and data for the normal report."""

    columns = [
        {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Data",
        },
        {
            "label": _("Salary"),
            "fieldname": "salary",
            "fieldtype": "Currency",
        },
        {
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Data",
        },
        {
            "label": _("Date"),
            "fieldname": "date",
            "fieldtype": "Date",
        },
    ]

    data = [
        {
            "employee": "Vishal",
            "salary": 120000,
            "department": "ECE",
            "date": "2016-03-11",
        },
        {
            "employee": "Mouli",
            "salary": 45000,
            "department": "CSE",
            "date": "2016-08-01",
        },
        {
            "employee": "Yogesh",
            "salary": 40000,
            "department": "ECE",
            "date": "2016-01-19",
        },
    ]

    return columns, data


def execute_snapshot_report(filters: dict | None = None):
    """Return columns and data for the snapshot report."""

    columns = get_columns()
    data = get_data()

    return columns, data


def get_columns() -> list[dict]:
    """Return columns for the snapshot report."""

    return [
        {
            "label": _("Column 1"),
            "fieldname": "column_1",
            "fieldtype": "Data",
        },
        {
            "label": _("Column 2"),
            "fieldname": "column_2",
            "fieldtype": "Int",
        },
    ]


def get_data() -> list[list]:
    """Return data for the snapshot report."""

    return [
        ["Row 1", 1],
        ["Row 2", 2],
    ]