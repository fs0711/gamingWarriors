# Python imports
from datetime import datetime
# Framework imports
from flask import Blueprint

# Local imports
from gwBackend.RfCardManagement.controllers.RfCardController import RfCardController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

rfcard_bp = Blueprint("rfcard_bp", __name__)

@rfcard_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__RFCARD,
    constants.OPTIONAL_FIELDS_LIST__RFCARD
)
def create_view(data):
    res = RfCardController.create_controller(data=data)
    return res

@rfcard_bp.route("/read", methods=["GET","POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    [constants.RFCARD__ASSIGNED,constants.RFCARD__ORGANIZATION]
)
def read_view(data):
    res = RfCardController.read_controller(data=data)
    return res

@rfcard_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    []
)
def update_view(data):
    return RfCardController.update_controller(data=data)

@rfcard_bp.route("/list_rfcards", methods=["GET","POST"])
# @decorators.is_authenticated
# @decorators.roles_allowed([])
@decorators.keys_validator(
    [],
    [constants.RFCARD__ASSIGNED,constants.RFCARD__ORGANIZATION]
)
def list_view(data):
    return RfCardController.get_rfcards(data=data)


@rfcard_bp.route("/list_by_org", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [constants.RFCARD__ORGANIZATION]
)
def list_card_by_org(data):
    res = RfCardController.get_rfcards_org(data=data)
    return res


@rfcard_bp.route("/get_card_id", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [constants.RFCARD__UID]
)
def list_card_by_uid(data):
    res = RfCardController.get_card_id_list(data=data)
    return res