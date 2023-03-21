# Python imports

# Framework imports
from flask import jsonify
from flask import render_template, redirect, request, Response
from datetime import datetime, timedelta

# Local imports
from gwBackend import app, config
from gwBackend.LeadsManagement.controllers.LeadsController import LeadsController
from gwBackend.generic.services.utils import constants, decorators
from gwBackend.UserManagement.views.users import users_bp
from gwBackend.BranchManagement.views.branch import branch_bp
from gwBackend.ClientsManagement.views.clients import clients_bp
from gwBackend.GameunitManagement.views.gameunit import gameunit_bp
from gwBackend.ReservationManagement.views.reservation import reservation_bp
from gwBackend.generic.services.utils import common_utils
from gwBackend.generic.services.utils.common_utils import current_user
from gwBackend.LeadsManagement.controllers.DashboardController import DashboardController
from gwBackend.LeadsManagement.controllers.DashboardController import DashboardFollow


# @app.route("/", methods=["GET"])
# def index_view():
#     return render_template('login.html')
# return "Server is running fine."

@app.route("/home", methods=["GET"])
# @decorators.logging
@decorators.is_authenticated
@decorators.keys_validator(
    [],
    constants.ALL_FIELDS_LIST__LEAD,
)
def dashboard_view(data):
    res = DashboardController.get_dashboard_stats()
    # res2 = DashboardFollow.read_follow(data=data)
    # obj = {'leads_count':'0',
    #     'follow_ups':'0'}
    # obj.update({'leads_count':res})
    # obj.update({'follow_ups':res2})
    return render_template('dashboard.html', **res)


@app.route("/addlead", methods=["GET"])
def addlead_view():
    return render_template('addlead.html')

@app.route("/api/static-data", methods=["GET"])
def static_data_view():
    return jsonify(constants.STATIC_DATA)


app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(branch_bp, url_prefix="/api/branch")
app.register_blueprint(clients_bp, url_prefix="/api/clients")
app.register_blueprint(gameunit_bp, url_prefix="/api/gameunit")
app.register_blueprint(reservation_bp, url_prefix="/api/reservation")
