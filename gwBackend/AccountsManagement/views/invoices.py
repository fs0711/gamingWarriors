# Python imports
from datetime import datetime
# Framework imports
from flask import Blueprint

# Local imports
from gwBackend.AccountsManagement.controllers.InvoiceController import InvoiceController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

invoice_bp = Blueprint("invoice_bp", __name__)

@invoice_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__INVOICE,
    constants.OPTIONAL_FIELDS_LIST__INVOICE
)
def create_view(data):
    res = InvoiceController.create_controller(data=data)
    return res

@invoice_bp.route("/read", methods=["GET", "POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__INVOICE
)
def read_view(data):
    res = InvoiceController.read_controller(data=data)
    return res

@invoice_bp.route("/pay", methods=["GET", "POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    [constants.ID]
)
def pay_view(data):
    res = InvoiceController.pay_controller(data=data)
    return res