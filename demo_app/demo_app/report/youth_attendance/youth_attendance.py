# Copyright (c) 2025, 1 and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [], []
	return columns, data


def get_columns():
	columns = [
		{
			"fieldname": "date",
			"label": "Date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "member",
			"label": "Member",
			"fieldtype": "Link",
			"options": "User",
			"width": 200
		},
		{
			"fieldname": "youth_group",
			"label": "Youth Group",
			"fieldtype": "Link",
			"options": "Youth Group",
			"width": 200
		},
		{
			"fieldname": "status",
			"label": "Status",
			"fieldtype": "Select",
			"options": "\nPresent\nAbsent\nExcused",
			"width": 100
		},
	]

	return columns