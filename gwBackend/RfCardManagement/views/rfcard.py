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

@rfcard_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    []
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

