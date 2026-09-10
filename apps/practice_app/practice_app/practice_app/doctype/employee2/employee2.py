# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee2(Document):
	
	def validate(self):
		if self.salary<15000:
			frappe.throw("salary must be greater than 15000")

	def before_save(self):
		if self.status=="":
			self.status = "Active"



@frappe.whitelist()
def check(self,id):
	doc = frappe.get_doc("Employee2",id)
	if doc.salary>40000:
		print("Senior Employee")
	else:
		print("Regular Employee")


@frappe.whitelist()
def totalyears(self,id):
	doc = frappe.get_doc("Employee2",id)
	total = 0
	for row in doc.skills:
		total = total + row.experience
	print(total)
	return total