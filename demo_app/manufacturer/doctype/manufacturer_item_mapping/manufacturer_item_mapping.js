// Copyright (c) 2026, Saiyyam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Manufacturer-Item Mapping", {
	refresh(frm) {

        if(!frm.doc.manufacturer) return

        let btn_label = "Disable Manufacturer"
        let status_val = 1
        
        if (frm.doc.is_blocked){
            btn_label = "Enable Manufacturer"
            status_val = 0
            frm.disable_form()
        } 
        else {
            cur_frm.enable_save()
        }
        
        frm.add_custom_button(btn_label,()=>{

            if(frm.is_dirty()) {
                frappe.throw("Please Save the document first")
            }

            frm.set_value("is_blocked", status_val)
            frm.save()
            frm.reload_doc()
        })
	},
});
