// Copyright (c) 2024, ALI RAZA and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Epences Report"] = {
	"filters": [
        {
            "fieldname": "petty_cash",
            "label": __("Petty Cash"),
            "fieldtype": "Link",
            "options": "Petty Cash",
            "default": null
        },
        {
            "fieldname": "employee_name",
            "label": __("Employee Name"),
            "fieldtype": "Data",
            "default": null
        },
        // {
        //     "fieldname": "month",
        //     "label": __("Month"),
        //     "fieldtype": "Data",
        //     "default": null
        // }
    ]
};
