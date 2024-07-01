// Copyright (c) 2024, ALI RAZA and contributors
// For license information, please see license.txt

frappe.ui.form.on('CSV File', {
    upload: function (frm) {
        if (!frm.doc.cvs_file) {
            frappe.msgprint(__('Please attach a file first.'));
            return;
        }
        frappe.call({
            method: 'petty_cash.petty_cash.doctype.csv_file.csv_file.read_csv',
            args: {
                docname: frm.doc.name
            },
            callback: function (r) {
                if (r.message) {
                    frm.set_value('text', r.message.raw_data);
                    frm.set_value('account_details', r.message.account_details);
                    frm.refresh_field('account_details');
                    frm.refresh_field('text');
                }
            }
        });
    }
});
