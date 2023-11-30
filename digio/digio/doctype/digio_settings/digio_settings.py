# Copyright (c) 2023, Wahni IT Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class DigioSettings(Document):
	def validate(self):
		self.validate_integration_fields()

	def validate_integration_fields(self):
		if not self.is_enabled:
			return

		if not self.url:
			frappe.throw(_("URL is required."))

		if not self.client_id:
			frappe.throw(_("Client ID is required."))
		
		if not self.client_secret:
			frappe.throw(_("Client secret is required."))
		