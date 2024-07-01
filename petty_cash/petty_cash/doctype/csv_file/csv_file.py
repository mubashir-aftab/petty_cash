import frappe
import csv
from frappe.model.document import Document
from frappe import _
from bs4 import BeautifulSoup

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

    def process_html_content(content):
        soup = BeautifulSoup(content, 'html.parser')
        tables = soup.find_all('table')
        all_table_data = []
        for table in tables:
            table_data = extract_table_data(table)
            if table_data:
                all_table_data.extend(table_data)
        return all_table_data

    def extract_table_data(table):
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = table.find_all('tr')
        table_data = []
        
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == len(headers):
                row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
                table_data.append(row_data)
        return table_data

    def process_csv_reader(reader):
        for row in reader:
            if row:
                detail = {
                    'Número de Clientes': row.get('Número de Clientes', '').strip(), 
                    'Nombre': row.get('Nombre', '').strip(),
                    'Producto': row.get('Producto', '').strip(),
                    'Moneda': row.get('Moneda', '').strip(),
                    'Saldo Inicial': row.get('Saldo Inicial', '').strip(),
                    'Saldo en Libros': row.get('Saldo en Libros', '').strip(),
                }
                account_details.append(detail)
                raw_data.append(row)

    def is_html(content):
        return '<table>' in content

    with open(file_path, mode='r', encoding='utf-8') as file:
        content = file.read()
        
        if is_html(content):
            # Process HTML-embedded CSV
            table_data = process_html_content(content)
            for data in table_data:
                account_details.append(data)
                raw_data.append(data)
        else:
            # Process simple CSV
            file.seek(0)  # Rewind the file to the beginning
            reader = csv.DictReader(content.splitlines())
            process_csv_reader(reader)

    formatted_details_list = []

    for detail in account_details:
        formatted_detail = ""
        for key, value in detail.items():
            if value:
                formatted_detail += f"{key}: {value}\n"
        formatted_details_list.append(formatted_detail.strip())  
    
    formatted_details = '\n\n\n'.join(formatted_details_list)
    raw_data_str = '\n'.join([str(row) for row in raw_data]) 

    frappe.msgprint(_("Raw Data:"))
    frappe.msgprint(raw_data_str)
    frappe.msgprint(_("Formatted Details:"))
    frappe.msgprint(formatted_details)
    
    return {
        'account_details': formatted_details,
        'raw_data': raw_data_str
    }
