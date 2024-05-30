# Copyright (c) 2024, ALI RAZA and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class PettyCash(Document):
    def before_insert(self):
        try:
            latest_expense = frappe.get_list('Expences', fields=['remaining_amount'], order_by='creation desc', limit=1)
            remaining_amount = 0
            if latest_expense:
                remaining_amount = latest_expense[0]['remaining_amount']
            else:
                frappe.msgprint('No Remaining Amount found to fetch Expences from.')
            
            self.remainings_of_last_month = remaining_amount
            total_amount = remaining_amount + self.amount
            # frappe.msgprint(('Total Amount: {0}').format(total_amount))
            self.total_petty_this_month = total_amount
        except Exception as e:
            frappe.throw('Error fetching remaining amount from Expenses: {0}').format(str(e))

		
