# Copyright (c) 2024, ALI RAZA and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Expences(Document):
	def validate(self):
            total_amount = sum(row.amount for row in self.months_expenses if row.amount is not None)
        #     frappe.msgprint(str(total_amount))
            self.total_amount = total_amount
            if self.amount is not None:
                   self.remaining_amount = self.amount - self.total_amount  
                #    frappe.msgprint(str(self.remaining_amount))
            # create a new document
        #     doc = frappe.get_doc('Petty Cash', self.petty_cash)
        #     doc.remainings_of_last_month=self.remaining_amount
        #     total_amount=doc.amount+doc.remainings_of_last_month
        #     doc.total_petty_this_month=total_amount
        #     doc.save()

        #     doc=frappe.set_value('Petty Cash', self.petty_cash,'remainings_of_last_month',self.remaining_amount)
                
        #     doc.remainings_of_last_month = self.remaining_amount
        #     frappe.msgprint(str(doc.remainings_of_last_month))
            

            for row in self.months_expenses:
                    if not row.receipt_image:
                            if not row.reason:
                                    frappe.throw(('Reason is mandatory when Receipt Image is empty in row {0}').format(row.idx))
        # pass