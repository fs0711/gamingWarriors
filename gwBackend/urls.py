# Python imports

# Framework imports
from flask import jsonify
from flask import render_template, redirect, request, Response
from datetime import datetime, timedelta

# Local imports
from gwBackend import app, config
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.UserManagement.views.users import users_bp
from gwBackend.BranchManagement.views.branch import branch_bp
from gwBackend.MembersManagement.views.members import members_bp
from gwBackend.GameunitManagement.views.gameunit import gameunit_bp
from gwBackend.ReservationManagement.views.reservation import reservation_bp
from gwBackend.AccountsManagement.views.accounts import accounts_bp
from gwBackend.RfCardManagement.views.rfcard import rfcard_bp
from gwBackend.AccountsManagement.views.invoices import invoice_bp
from gwBackend.OrganizationsManagement.views.organizations import organizations_bp
from gwBackend.generic.services.utils import common_utils
from gwBackend.generic.services.utils.common_utils import current_user


@app.route("/", methods=["GET"])
def index_view():
    return "Server is running fine."


@app.route("/api/static-data", methods=["GET"])
def static_data_view():
    return jsonify(constants.STATIC_DATA)


app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(branch_bp, url_prefix="/api/branch")
app.register_blueprint(members_bp, url_prefix="/api/members")
app.register_blueprint(gameunit_bp, url_prefix="/api/gameunit")
app.register_blueprint(reservation_bp, url_prefix="/api/reservation")
app.register_blueprint(rfcard_bp, url_prefix="/api/rfid")
app.register_blueprint(organizations_bp, url_prefix="/api/organization")
app.register_blueprint(accounts_bp, url_prefix="/api/accounts")
app.register_blueprint(invoice_bp, url_prefix="/api/invoice")

