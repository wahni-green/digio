import frappe
from frappe import _
import requests
from digio.utils.digio import Digio
import base64



def upload_to_digio(file):
    digio = Digio()
    
    try:
        response = requests.post(digio.id_card_ocr, headers=digio.headers)
        
    except Exception as e:
        frappe.msgprint(str(e))



    # if not digio.is_enabled():
    #     return file.save_file_on_filesystem()

    # frappe.msgprint(_("Uploading to Azure Blob Storage"), alert=True)
    # if isinstance(file._content, str):
    #     file._content = file._content.encode()

    # file_name, url = digio.upload_file(file)
    # file.file_url = digio.get_sas_url(file_name)
    # file.blob_url = url
    # file.file_name = file_name
    # frappe.msgprint(_("Uploaded to Azure Blob Storage"), alert=True)
