# Copyright (c) 2023, Wahni It Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from digio.utils import upload_to_digio

class DigioSettings(Document):
	def validate(self):
		self.validate_connection_string()
		upload_to_digio(file="")
	
	def validate_connection_string(self):
		if not self.is_enabled:
			return

		if not self.client_id:
			frappe.throw(_("Client ID is required."))
		
		if not self.client_secret:
			frappe.throw(_("Client secret is required."))
		