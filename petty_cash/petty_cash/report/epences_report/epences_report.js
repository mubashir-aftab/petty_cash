// Copyright (c) 2024, ALI RAZA and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Epences Report"] = {
    onload: function (report) {
        var defaultCustomer = frappe.defaults.get_default("customer");
        
        
                
                frappe.db.get_doc('Expences', expenses.name)
                    .then(doc => {
                        if (doc.items && doc.items.length > 0) {
                            let item = doc.items[0];
                            console.log(doc);
                            
                            localStorage.setItem("customer", JSON.stringify({ 
                                employee_name: doc.employee_name,
                                desigination:doc.desigination,
                                // month:doc.month,
                                // amount:doc.amount,
                                // total_amount:total_amount,
                                // remaining_amount:remaining_amount,
                                // item_name: item.item_name,
                                // item_code: item.item_code,
                                // amount: item.amount
                            }));
                        }
                    });
	},
	"filters": [
        {
            "fieldname": "petty_cash",
            "label": __("Petty Cash"),
            "fieldtype": "Link",
            "options": "Petty Cash",
            "default": null
        },
        {
            "fieldname": "from_date",
            "label": __("From_Date"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "to_date",
            "label": __("To_Date"),
            "fieldtype": "Date"
        },
    ]
};
