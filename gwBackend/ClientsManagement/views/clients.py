# Python imports
import os
import re
import pandas as pd
from datetime import datetime
# Framework imports
from flask import Blueprint, redirect, url_for, redirect, render_template, request

# Local imports
from gwBackend.ClientsManagement.controllers.ClientsController import ClientsController
from gwBackend.LeadsManagement.controllers.FollowUpController import FollowUpController
from gwBackend.UserManagement.controllers.UserController import UserController
from gwBackend.generic.services.utils import constants, decorators, common_utils
from gwBackend.config import config

clients_bp = Blueprint("clients_bp", __name__)

@clients_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__CLIENTS,
    constants.REQUIRED_FIELDS_LIST__CLIENTS
)
def create_view(data):
    res = ClientsController.create_controller(data=data)
    return res


# @clients_bp.route("/read", methods=["GET", "POST"])
# @decorators.is_authenticated
# @decorators.keys_validator()
# def read_view(data):
#     if request.method == "POST":
#         data = request.form
#     res = ClientsController.read_controller(data=data)
#     return res
@clients_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__CLIENTS,
)
def read_view(data):
    res = ClientsController.read_controller(data=data)
    return res

@clients_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__CLIENTS,
)
def update_view(data):
    return ClientsController.update_controller(data=data)

