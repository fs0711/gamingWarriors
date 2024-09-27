# Python imports

# Framework imports
from flask import Blueprint, render_template, request

# Local imports
from gwBackend.UserManagement.controllers.UserController import UserController
from gwBackend.generic.services.utils import constants, decorators, response_codes, response_utils, common_utils


users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/create", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    constants.REQUIRED_FIELDS_LIST__USER,
    constants.OPTIONAL_FIELDS_LIST__USER,
)
def create_view(data):
    return UserController.create_controller(data=data)


@users_bp.route("/read", methods=["GET"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__USER,
)
def read_view(data):
    res = UserController.read_controller(data=data)
    return res


@users_bp.route("/update", methods=["PUT"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__USER,
)
def update_view(data):
    return UserController.update_controller(data=data)


@users_bp.route("/suspend", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [constants.ID]
)
def suspend_view(data):
    res = UserController.suspend_controller(data=data)
    return res

@users_bp.route("/login", methods=["POST"])
@decorators.logging
@decorators.keys_validator(constants.LOGIN_REQUIRED_FIELDS_LIST, [])
def login_user_view(data):
    res = UserController.login_controller(data=data)
    return res

@users_bp.route("/login/<platform>", methods=["POST"])
@decorators.logging
@decorators.keys_validator(constants.LOGIN_REQUIRED_FIELDS_LIST, [],
                           request_form_data=False)
def loginmobile_user_view(data, platform):
    data = common_utils.posted()
    return UserController.login_controller(data=data, platform=platform)

@users_bp.route("/logout", methods=["GET"])
@decorators.logging
@decorators.is_authenticated
@decorators.keys_validator()
def logout_user_view(_):
    res = UserController.logout_controller()
    return render_template("logout.html", **res)

@users_bp.route("/list", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [constants.USER__ROLE],
)
def list_view(data):
    res = UserController.get_user_list(data=data)
    return res

@users_bp.route("/child_list", methods=["POST"])
@decorators.is_authenticated
@decorators.roles_allowed([constants.ROLE_ID_ADMIN,constants.ROLE_ID_OWNER, constants.ROLE_ID_CLIENT])
@decorators.keys_validator(
    [constants.ID]
)
def child_view(data):
    res = UserController.get_users_childs_list(data=data)
    return res

@users_bp.route("/all_users", methods=["GET"])
# @decorators.is_authenticated
# @decorators.roles_allowed([])
@decorators.keys_validator()
def list_users(data):
    return UserController.get_all_users()