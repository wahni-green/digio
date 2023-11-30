# Copyright (c) 2023, Wahni IT Solutions and contributors
# For license information, please see license.txt

import frappe
from digio.utils.digio import Digio


@frappe.whitelist()
def upload_to_digio(document_type, file_url):
	file = frappe.db.get_value("File", {"file_url": file_url})
	if file:
		digio = Digio()
		return digio.get_data(document_type, file)
	return {}
