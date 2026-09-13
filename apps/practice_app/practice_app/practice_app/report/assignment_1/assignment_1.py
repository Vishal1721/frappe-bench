# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

# import frappe
from frappe import _


def execute(filters: dict | None = None):
    """Return columns and data for the report.

    This is the main entry point for the report. It accepts the filters as a
    dictionary and should return columns and data. It is called by the framework
    every time the report is refreshed or a filter is updated.
    """
    columns = [
        {
            "label": "Employee",
            "fieldname": "employee",
            "fieldtype": "Data"
        },
        {
            "label": "Salary",
            "fieldname": "salary",
            "fieldtype": "Currency"
        },
        {
            "label": "Department",
            "fieldname": "department",
            "fieldtype": "Data"
        },
        {
            "label": "Date",
            "fieldname":"date",
            "fieldtype": "Date"
        }

    ]

    data = [
        {
            "employee": "Vishal",
            "salary": 120000,
            "department": "ECE",
            "date":"2016-03-11"
        },
        {
            "employee": "Mouli",
            "salary": 45000,
            "department": "CSE",
            "date":"2016-08-01"
        },
        {
            "employee": "Yogesh",
            "salary": 40000,
            "department": "ECE",
            "date":"2016-01-19"
        }
    ]


    return columns, data

def execute_snapshot_report(filters: dict | None = None):
    """Return columns and data for the report.

    This is the main entry point for snapshot report. When 'Synced
    Report' is enabled in report, framework will call this method
    every time the report is refreshed or a filter is updated. It
    accepts the same filters as normal execute. But a utility method -
    get_latest_sync, is also imported.

    """
    from frappe.database.duckdb.database import get_latest_sync

    columns = get_columns()
    data = get_data()

    return columns, data

def get_columns() -> list[dict]:
    """Return columns for the report.

    One field definition per column, just like a DocType field definition.
    """
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
    """Return data for the report.

    The report data is a list of rows, with each row being a list of cell values.
    """
    return [
        ["Row 1", 1],
        ["Row 2", 2],
    ]
