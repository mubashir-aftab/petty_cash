# Copyright (c) 2024, ALI RAZA and contributors
# For license information, please see license.txt

# In your report's script section (usually found under "Edit Script" in the report settings)

import frappe
def execute(filters=None):
    columns, data = [], []
    
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        {"label": ("Petty Cash"), 
         "fieldname": "petty_cash", 
         "fieldtype": "Link", 
         "options": "Petty Cash", 
         "width": 100
        },
        {"label": ("Employee Name"), 
         "fieldname": "employee_name", 
         "fieldtype": "Data", 
         "width": 150
        }
        ,
        {"label": ("Desigination"), 
         "fieldname": "designation", 
         "fieldtype": "Data", 
         "width": 150
        },
        {"label": ("Month"), 
         "fieldname": "month", 
         "fieldtype": "Date", 
         "width": 100
        },
        {"label": ("Amount"), 
         "fieldname": "amount", 
         "fieldtype": "Currency", 
         "width": 100
        },
        {"label": ("Expense Date"), 
         "fieldname": "expense_date", 
         "fieldtype": "Date", 
         "width": 100
        },
        {"label": ("Receipt Image"), 
         "fieldname": "receipt_image", 
         "fieldtype": "Attach Image", 
         "width": 150
        },
        {"label": ("Expense Category"), 
         "fieldname": "expense_category", 
         "fieldtype": "Data", 
         "width": 120
        },
        {"label": ("Expense Amount"), 
		"fieldname": "expense_amount", 
        "fieldtype": "Currency", 
        "width": 100
        },
        {"label": ("Reason"), 
         "fieldname": "reason", 
         "fieldtype": "Data", 
         "width": 150
        },
        {"label": ("Total Amount"), 
         "fieldname": "total_amount", 
         "fieldtype": "Currency", 
         "width": 120
        },
        {"label": ("Remaining Amount"), 
         "fieldname": "remaining_amount", 
         "fieldtype": "Currency", 
         "width": 120
        }
    ]

def get_data(filters):
    data = []
    conditions = {"docstatus": ("<", 2)}

    if filters.get("petty_cash"):
        conditions["petty_cash"] = filters.get("petty_cash")
    if filters.get("employee_name"):
        conditions["employee_name"] = filters.get("employee_name")
    if filters.get("from_date") and filters.get("to_date"):
        conditions["expense_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]
    
    expenses = frappe.get_all('Expences',filters=conditions, fields=['name', 'petty_cash', 'employee_name', 'month', 'amount', 'total_amount', 'remaining_amount','desigination'])
    for exp in expenses:
        # frappe.msgprint(f"{len(exp.desigination)}")
        # frappe.msgprint(exp.month)
        
        months_expenses = frappe.get_all('Expenses Child', filters={'parent': exp.name}, fields=['expense_date', 'receipt_image', 'expense_category', 'amount', 'reason'])
        for child in months_expenses:
            data.append({
            "designation":exp.desigination,
            "petty_cash": exp.petty_cash,
            "employee_name": exp.employee_name,
            "month": exp.month,
            "amount": exp.amount,
            "expense_date": child.expense_date,
            "receipt_image": child.receipt_image,
            "expense_category": child.expense_category,
            "expense_amount": child.amount,
            "reason": child.reason,
            "total_amount": exp.total_amount,
            "remaining_amount": exp.remaining_amount
        })
            
    
    return data
