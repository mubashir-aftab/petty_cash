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
        if not headers:  # If no headers, find the first row's cells as headers
            headers = [td.get_text(strip=True) for td in table.find('tr').find_all('td')]
        rows = table.find_all('tr')[1:]  # Skip header row
        table_data = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) == len(headers):
                row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
                table_data.append(row_data)
        return table_data

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
            for row in reader:
                account_details.append(row)
                raw_data.append(row)

    formatted_details_list = []

    for detail in account_details:
        formatted_detail = ""
        currency = detail.get('Moneda')
        card_number = detail.get('Número de Tarjeta')
        reference_number = detail.get('Número de Referencia')
        if currency:
            formatted_detail += f"Moneda : {currency}\n"
        if card_number:
            formatted_detail += f"Número de Tarjeta: {card_number}\n"
        if reference_number:
            formatted_detail += f"Número de Referencia: {reference_number}\n"
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
