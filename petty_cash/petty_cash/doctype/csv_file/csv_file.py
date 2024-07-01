import frappe
import csv
from frappe.model.document import Document
from frappe import _
from bs4 import BeautifulSoup  # Assuming BeautifulSoup is installed

class CSVFile(Document):
    pass

@frappe.whitelist()
def read_csv(docname):
    doc = frappe.get_doc('CSV File', docname)
    file_url = doc.cvs_file
    
    if not file_url:
        frappe.throw(_('No file attached'))
    
    file_path = frappe.get_site_path('public', file_url.lstrip('/'))
    
    account_details = []
    raw_data = []
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row:
                detail = {
                    'Número de Clientes': row.get('Número de Clientes', '').strip(), 
                    'Nombre': row.get(' Nombre', '').strip(),
                    'Producto': row.get(' Producto', '').strip(),
                    'Moneda': row.get(' Moneda', '').strip(),
                    'Saldo Inicial': row.get(' Saldo Inicial', '').strip(),
                    'Saldo en Libros': row.get(' Saldo en Libros', '').strip(),
                }
                account_details.append(detail)
                raw_data.append(row)
    
    formatted_details_list = []

    for detail in account_details:
        formatted_detail = ""
        for key, value in detail.items():
            if value:
                formatted_detail += f"{key}: {value}\n"
        formatted_details_list.append(formatted_detail.strip())  
    
    formatted_details = '\n\n'.join(formatted_details_list)
    
    raw_data_str = '\n'.join([str(row) for row in raw_data]) 
    
    # Example: Web crawling to extract data from HTML content
    extracted_data = []
    for row in raw_data:
        html_content = row.get('HTML_content_column_name', '')  # Adjust column name
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            # Example extraction from HTML content
            extracted_value = soup.find('div', class_='extracted-data').text.strip()  # Adjust as per your HTML structure
            extracted_data.append(extracted_value)
    
    frappe.msgprint(_("Formatted Details:"))
    frappe.msgprint(formatted_details)
    frappe.msgprint(_("Raw Data:"))
    frappe.msgprint(raw_data_str)
    frappe.msgprint(_("Extracted Data:"))
    frappe.msgprint("\n".join(extracted_data))
    
    return {
        'account_details': formatted_details,
        'raw_data': raw_data_str,
        'extracted_data': "\n".join(extracted_data)
    }
