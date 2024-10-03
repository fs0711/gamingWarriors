# Python imports
import os
# Framework imports
from flask import Blueprint, request

# Local imports
from gwBackend.MembersManagement.controllers.MembersController import MembersController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.config import config

members_bp = Blueprint("members_bp", __name__)

@members_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__MEMBERS,
    constants.REQUIRED_FIELDS_LIST__MEMBERS
)
def create_view(data):
    res = MembersController.create_controller(data=data)
    return res


@members_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__MEMBERS,
)
def read_view(data):
    res = MembersController.read_controller(data=data)
    return res

@members_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    []
)
def update_view(data):
    return MembersController.update_controller(data=data)


@members_bp.route("/list_members", methods=["GET"])
@decorators.is_authenticated
# @decorators.roles_allowed([])
@decorators.keys_validator()
def list_view(data):
    return MembersController.get_members()


@members_bp.route("/list_members_id", methods=["GET"])
@decorators.is_authenticated
# @decorators.roles_allowed([])
@decorators.keys_validator()
def list_view_id(data):
    return MembersController.get_members_id()