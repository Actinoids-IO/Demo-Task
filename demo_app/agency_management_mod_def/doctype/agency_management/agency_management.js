// Copyright (c) 2026, Saiyyam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agency Management", {
	refresh(frm) {
        if(frm.doc.items && frm.doc.items.length > 0){
            let btn_label = "Disable Agent"
            let status_val = "In Active"
            
            if (frm.doc.status == "In Active"){
                btn_label = "Enable Agent"
                status_val = "Active"
            }
            frm.add_custom_button(btn_label,()=>{
                frm.set_value("status", status_val)
                frm.save()
            })

            if (frm.doc.status == "Active"){
                frm.add_custom_button("Create Supplier",()=>{
                    frappe.model.open_mapped_doc({
						method: "demo_app.agency_management_mod_def.doctype.agency_management.agency_management.create_supplier",
						frm : cur_frm
                    
					});

                })
            }


        }
	},
});
