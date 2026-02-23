# Copyright (c) 2026, Saiyyam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ManufacturerItemMapping(Document):
	def validate(self):
		manufacturer_item_dict = frappe._dict()
		for row in self.items:
			if manufacturer_item_dict.get(row.manufacturer) and manufacturer_item_dict.get(row.manufacturer) == row.item_code:
				frappe.throw("Manufacturer, Item code   pair has to be unique")
				
			if frappe.db.exists("Manufacturer Item", { "item_code" : row.item_code, "manufacturer" : row.manufacturer}):
				frappe.throw("Manufacturer, Item code pair has to be unique")

			manufacturer_item_dict.update({ row.manufacturer : row.item_code})
			if not row.part_number:
				row.part_number = row.item_code

@frappe.whitelist()
def get_manufacturer_items():
    item_code = frappe.form_dict.get("item_code")
    if not item_code:
        return []
    
    return frappe.db.get_all("Manufacturer Item", { "item_code" : item_code }, ['manufacturer', 'item_code', 'part_number', 'gtin']) or []
