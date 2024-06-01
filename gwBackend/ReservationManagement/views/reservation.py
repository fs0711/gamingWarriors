# Python imports

# Framework imports
from flask import Blueprint, request

# Local imports
from gwBackend.ReservationManagement.controllers.ReservationController import ReservationController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

reservation_bp = Blueprint("reservation_bp", __name__)

@reservation_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__RESERVATION,
    constants.REQUIRED_FIELDS_LIST__RESERVATION
)
def create_view(data):
    res = ReservationController.create_controller(data=data)
    return res

@reservation_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.REQUIRED_FIELDS_LIST__RESERVATION,
)
def read_view(data):
    res = ReservationController.read_controller(data=data)
    return res

@reservation_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.REQUIRED_FIELDS_LIST__RESERVATION,
)
def update_view(data):
    return ReservationController.update_controller(data=data)

