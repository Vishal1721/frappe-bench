# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


@frappe.whitelist()
def get_asset_detail(asset):
    doc = frappe.get_doc('Asset',asset)
    quantity = doc.available_quantity
    rate = doc.rate

    return {
        "quantity":quantity,
        "rate":rate
    }
class AssetRequestItem(Document):
    pass