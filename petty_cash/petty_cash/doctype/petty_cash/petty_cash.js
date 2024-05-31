// Copyright (c) 2024, ALI RAZA and contributors
// For license information, please see license.txt

frappe.ui.form.on('Petty Cash', {
	after_save: function(frm) {
	frm.refresh_field('remainings_petty');
	}
});
