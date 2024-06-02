# Python imports
import os
# Framework imports
from flask import Blueprint, request

# Local imports
from gwBackend.MembersManagement.controllers.ProfilesController import ProfilesController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

profiles_bp = Blueprint("profiles_bp", __name__)

@profiles_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__PROFILE,
    constants.REQUIRED_FIELDS_LIST__PROFILE
)
def create_view(data):
    res = ProfilesController.create_controller(data=data)
    return res


@profiles_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    []
)
def read_view(data):
    res = ProfilesController.read_controller(data=data)
    return res

@profiles_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    []
)
def update_view(data):
    return ProfilesController.update_controller(data=data)

