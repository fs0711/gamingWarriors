# Framework imports
from flask import Flask
from flask_moment import Moment
from flask_cors import CORS
from flask_bcrypt import Bcrypt
# Local imports
from gwBackend.generic.database import initialize_db
from gwBackend.config import config


def register_scripts():
    from gwBackend.scripts import run_scripts
    from gwBackend.scripts.JunkFollowUpLeadHistoryRemoval import junk_follow_up_lead_history_removal
    run_scripts(execute_create_admin_user_if_not_exists=True, execute_phone_number_format_correction=False,
                execute_update_id_field=False, execute_find_empty_leads=False,
                execute_junk_follow_up_lead_history_removal=False, update_leads_execute=False, execute_find_missing=False, 
                execute_report_generator=False)
    # Routing
    import gwBackend.urls


# application objects
app = Flask(__name__)
CORS(app)
app.config["MONGODB_HOST"] = config.MONGO_DB_URI
app.config["UPLOAD_FOLDER"] = config.upload_files_path
initialize_db(app)
moment = Moment(app)
bcrypt = Bcrypt(app)
app.config.update(config.MAIL_SETTINGS)
register_scripts()