# Python imports
from datetime import datetime
# Framework imports
from flask import Blueprint

# Local imports
from gwBackend.AccountsManagement.controllers.AccountsController import AccountsController
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
@decorators.keys_validator()
def read_view(data):
    res = AccountsController.read_controller(data=data)
    return res


@accounts_bp.route("/list_transactions", methods=["GET"])
@decorators.is_authenticated
# @decorators.roles_allowed([])
@decorators.keys_validator()
def list_transactions(data):
    return AccountsController.get_transactions()


# @accounts_bp.route("/update", methods=["PUT"])
# @decorators.is_authenticated
# @decorators.keys_validator(
#     []
# )
# def update_view(data):
#     return RfCardController.update_controller(data=dataAccountsController.route("/list_rfcards", methods=["GET","POST"])
# @decorators.is_authenticated
# # @decorators.roles_allowed([])
# @decorators.keys_validator(
#     [],
#     [constants.RFCARD__ASSIGNED,constants.RFCARD__ORGANIZATION]
# )
# def list_vAccountsController):
#     return RfCardController.get_rfcards(data=data)