# Copyright (c) 2023, Wahni IT Solutions and contributors
# For license information, please see license.txt

import frappe
import base64
import requests
from requests.auth import HTTPBasicAuth
import io


DOCUMENT_MAPPING = {
	"ID": "id_card_ocr"
}

class Digio():
	def __init__(self) -> None:
		self.settings = frappe.get_cached_doc("Digio Settings")
		self.auth = HTTPBasicAuth(self.settings.client_id, self.settings.get_password("client_secret"))
		self.headers = {'Content Type': "multipart/form-data"}

	def get_data(self, document_type, file):
		method = DOCUMENT_MAPPING.get(document_type, "id_card_ocr")
		return getattr(self, method)(file)

	def id_card_ocr(self, file):
		url = f"{self.settings.url}/v3/client/kyc/analyze/file/idcard"
		payload = {
			"front_part": io.BytesIO(frappe.get_doc("File", file).get_content()),
		}
		response = requests.post(url, auth=self.auth, files=payload)
		response.raise_for_status()
		return response.json()

