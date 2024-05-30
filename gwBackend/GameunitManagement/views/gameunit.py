# Python imports
import os
import re
from datetime import datetime
# Framework imports
from flask import Blueprint, redirect, url_for, redirect, render_template, request

# Local imports
from gwBackend.GameunitManagement.controllers.GameunitController import GameunitController
from gwBackend.LeadsManagement.controllers.FollowUpController import FollowUpController
from gwBackend.UserManagement.controllers.UserController import UserController
from gwBackend.generic.services.utils import constants, decorators, common_utils
from gwBackend.config import config

gameunit_bp = Blueprint("gameunit_bp", __name__)

@gameunit_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__GAMEUNIT,
    constants.REQUIRED_FIELDS_LIST__GAMEUNIT
)
def create_view(data):
    res = GameunitController.create_controller(data=data)
    return res

@gameunit_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.REQUIRED_FIELDS_LIST__GAMEUNIT,
)
def read_view(data):
    res = GameunitController.read_controller(data=data)
    return res

@gameunit_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.REQUIRED_FIELDS_LIST__GAMEUNIT,
)
def update_view(data):
    return GameunitController.update_controller(data=data)

