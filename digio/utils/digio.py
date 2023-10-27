# Copyright (c) 2023, Wahni It Solutions and contributors
# For license information, please see license.txt
import frappe
import base64


class Digio():
	def __init__(self) -> None:
		self.settings = frappe.get_cached_doc("Digio Settings")
		# self.pwd = BlobServiceClient.from_connection_string(
		# 	self.settings.get_password("client_secret")
		# )

		self.token = base64.b64encode(('{}:{}'.format(self.settings.client_id, self.settings.client_secret)).encode('utf-8')).decode('utf-8')
		

		self.headers = {
			'Authorization': self.token ,
			'Content Type' : "multipart/form-data"
		}

	def id_card_ocr(self):
		url = f"{self.settings.url}/v3/client/kyc/analyze/file/idcard"
		# frappe.msgprint(str(url))
		# return self.url
