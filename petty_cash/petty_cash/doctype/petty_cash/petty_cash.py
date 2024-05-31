# Copyright (c) 2024, ALI RAZA and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

from frappe.model.document import Document
import frappe

class PettyCash(Document):
    def before_insert(self):
#         try:
#             latest_expense = frappe.get_list('Expences',filters={'petty_cash':self.name}, fields=['remaining_amount'])
#             # remaining_amount = 0
#             remaining_amount=latest_expense
#             # if latest_expense:
#             #     remaining_amount = latest_expense[0]['remaining_amount']
#             # else:
#             #     frappe.msgprint('No Remaining Amount found to fetch Expences from.')
            
#             self.remainings_petty = remaining_amount
#             total_amount = remaining_amount + self.amount
#             frappe.msgprint(remaining_amount)
#             self.total_petty_this_month = total_amount
#         except Exception as e:
#             frappe.throw('Error fetching remaining amount from Expenses: {0}').format(str(e))
     pass
		
