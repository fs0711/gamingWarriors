# Python imports
from datetime import datetime
# Framework imports
from flask import Blueprint

# Local imports
from gwBackend.AccountsManagement.controllers.AccountController import AccountsController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

accounts_bp = Blueprint("accounts_bp", __name__)

@accounts_bp.route("/credit", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__ACCOUNTS,
    constants.OPTIONAL_FIELDS_LIST__ACCOUNTS
)
def create_view(data):
    res = AccountsController.create_controller(data=data)
    return res

@accounts_bp.route("/read", methods=["GET","POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__ACCOUNTS
)
def read_view(data):
    res = AccountsController.read_controller(data=data)
    return res

@accounts_bp.route("/list_transactions", methods=["GET","POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    [constants.ORGANIZATION,constants.BRANCH,constants.ACCOUNTS__START_DATE,constants.ACCOUNTS__END_DATE],
)
def list_by_user(data):
    return AccountsController.list_controller(data=data)


