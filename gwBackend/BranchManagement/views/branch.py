# Python imports
import os
import re
import pandas as pd
from datetime import datetime
# Framework imports
from flask import Blueprint, redirect, url_for, redirect, render_template, request

# Local imports
from gwBackend.generic.services.utils import constants, decorators, common_utils
from gwBackend.BranchManagement.controllers import BranchController
from gwBackend.config import config

branch_bp = Blueprint("branch_bp", __name__)


@branch_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__BRANCH,
    constants.REQUIRED_FIELDS_LIST__BRANCH,
    request_form_data=False
)
def branch_create_view(data):
    rest = BranchController.create_controller(data=data)
    return (rest)


@branch_bp.route("/read", methods=["GET", "POST"])
@decorators.is_authenticated
@decorators.keys_validator()
def read_view(data):
    if request.method == "POST":
        data = request.form
    res = BranchController.read_controller(data=data)
    return res


@branch_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
# @decorators.roles_allowed([constants.ROLE_ID_ADMIN])
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__LEAD,
)
def update_view(data):
    return BranchController.update_controller(data=data)

@branch_bp.route("/search", methods=["POST", "GET"])
@decorators.is_authenticated
@decorators.keys_validator()
def search_view(data):
    if request.method == "POST":
        data = request.form
        res = BranchController.search_controller(data=data)
        return render_template("find_leads.html", **res)
    
    return render_template("find_leads.html")
