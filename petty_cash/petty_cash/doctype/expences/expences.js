// Copyright (c) 2024, ALI RAZA and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expences', {
    month: function(frm) {
            let _date = new Date(frm.doc.month);
            let month = _date.getMonth() + 1;
            let year = _date.getFullYear();
            
            // Calculate the start date
            let start_date = year + '-' + month + '-01';
            
            // Calculate the end date by getting the first day of the next month and subtracting one day
            // let next_month = new Date(year, month, 1); // This will be the first day of the next month
            // next_month.setDate(next_month.getDate() - 1); // Subtract one day to get the last day of the current month
            
            // let end_date = next_month.toISOString().split('T')[0];
            let end_date = year + '-' + month + '-31';
            
            console.log(month, start_date, end_date);

            frm.set_query('petty_cash', function() {
                return {
                    filters: {
                        'month': ['between', [start_date, end_date]]
                    }
                };
            });
        
    }
    // ,
    // onload: function(frm){
    //     frm.set_query('petty_cash', function () {
    //         let month = new Date().getMonth() + 1; 
    //         // let month = frm.doc.month.getMonth() + 1; 

    //         let year = new Date().getFullYear(); 
    //         // let year = frm.doc.month.getFullYear(); 
    //         let start_date = year + '-' + month + '-01';
    //         let end_date = year + '-' + month + '-31';
    //         return {
    //             filters: {
    //                 'month': ['between', [start_date, end_date]]
    //             }
    //         };
    //     });
        
    // }
});