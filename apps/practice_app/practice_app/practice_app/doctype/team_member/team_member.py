# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class TeamMember(WebsiteGenerator):
    def get_context(self, context):
        context.member = self.member_name
        context.email = self.email

        return context