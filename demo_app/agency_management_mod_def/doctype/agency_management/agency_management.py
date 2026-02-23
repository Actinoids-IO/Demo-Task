# Copyright (c) 2026, Saiyyam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class AgencyManagement(Document):
	pass


@frappe.whitelist()
def create_supplier(source_name, target_doc = "Supplier"):
	agency_doc = frappe.get_doc("Agency Management", source_name)
	supplier_doc = frappe.new_doc("Supplier")
	supplier_doc.update(
		{"supplier_name" : source_name,
					"supplier_type" : "Company",
					"country" : "India"
	})

	supplier_doc.save(ignore_permissions=True)
	agency_doc.status = "Supplier"
	agency_doc.save(ignore_permissions=True)
	return supplier_doc
