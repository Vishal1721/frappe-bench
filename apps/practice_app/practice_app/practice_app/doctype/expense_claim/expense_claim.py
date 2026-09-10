# Copyright (c) 2026, vishal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def validate(self):
		self.validate_manager_approval(self)
		for row in self.items:
			if row.amount<0:
				frappe.throw("Negative amount should not be allowed")
	
	def before_save(self):
		self.calculate_amount()
	
	def calculate_amount(self):
		total =0 
		for row in self.items:
			total += row.amount

		self.total_amount = total

		if self.total_amount > 50000:
			self.status = "Pending Approval"
		
	def validate_manager_approval(self):
		if self.status!="Approved":
			return
		
		doc = frappe.get_doc('Employee3',self.employee)
		current_user = frappe.session.user
		employee = frappe.db.get_value('Employee3',{"email":current_user},"name")
		if doc.manager != employee:
			frappe.throw("Current user has not access to approved")
		
	@frappe.whitelist()
	def get_employee_expense_summary(employee):
		approvalAmount =0
		rejectedAmount =0 
		list1 = frappe.db.get_all('Expense Claim',filters={"employee":employee},fields=["status","total_amount"])
		count = frappe.db.count(
			"Expense Claim",
			{"employee": employee}
		)
		for x in list1:
			if x.status=="Approved":
				approvalAmount += x.total_amount
			elif x.status == "Rejected":
				rejectedAmount += x.total_Amount
		return {
			'count':count,
			'approvalAmount':approvalAmount,
			'rejectedAmount' : rejectedAmount
		}



