# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils
from gwBackend.UserManagement.models.User import User

class Members(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.CLIENT__NAME: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__NIC: [{"rule": "datatype", "datatype": str}],
            constants.CLIENT__PHONE_NUMBER: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.CLIENT__PHONE_NUMBER,
                },
            ],
            constants.CLIENT__EMAIL_ADDRESS: [{"rule": "email"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__CARD_NUMBER: [{"rule": "datatype", "datatype": str}],
            constants.CLIENT__MEMBERSHIP_LEVEL: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__CITY: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__CREDIT: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__REWARD_POINTS: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.CLIENT__GAME_HISTORY: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],

        }

    @classmethod
    def update_validation_rules(cls): return {

    }

    client_id = db.SequenceField(value_decorator='CL-{}'.format)
    name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    email_address = db.StringField(reuired=True)
    city = db.StringField(required=True)
    nic = db.StringField(required=True)
    card_number = db.StringField(required=True)
    membership_level = db.StringField(required=True)
    credit = db.StringField(required=True)
    reward_points = db.StringField(required=True)
    game_history = db.StringField(required=True)


    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.CLIENT__ID: self[constants.CLIENT__ID],
            constants.CLIENT__NAME: self[constants.CLIENT__NAME],
            constants.CLIENT__NIC: self[constants.CLIENT__NIC],
            constants.CLIENT__PHONE_NUMBER: self[constants.CLIENT__PHONE_NUMBER],
            constants.CLIENT__EMAIL_ADDRESS: self[constants.CLIENT__EMAIL_ADDRESS],
            constants.CLIENT__CITY: self[constants.CLIENT__CITY],
            constants.CLIENT__CARD_NUMBER: self[constants.CLIENT__CARD_NUMBER],
            constants.CLIENT__MEMBERSHIP_LEVEL: self[constants.CLIENT__MEMBERSHIP_LEVEL],
            constants.CLIENT__CREDIT: self[constants.CLIENT__CREDIT],
            constants.CLIENT__REWARD_POINTS: self[constants.CLIENT__REWARD_POINTS],
            constants.CLIENT__GAME_HISTORY: self[constants.CLIENT__GAME_HISTORY],
            constants.STATUS: self[constants.STATUS],
            # constants.CLIENT__ASSIGNED_TO: self[constants.CLIENT__ASSIGNED_TO].fetch().name,
            # constants.CLIENT__ASSIGNED_BY: self[constants.CLIENT__ASSIGNED_BY].fetch().name,
            # constants.CLIENT__TRANSFERED: self[constants.CLIENT__TRANSFERED] if self[constants.CLIENT__TRANSFERED] else False,
            constants.CREATED_BY: self.created_by.fetch().name,
            constants.CREATED_ON: self[constants.CREATED_ON],
            constants.UPDATED_ON: self[constants.UPDATED_ON],
            # constants.CLIENT__TRANSFERED_ON: self[constants.CLIENT__TRANSFERED_ON] if self[constants.CLIENT__TRANSFERED_ON] else False
        }

    def display_min(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.CLIENT__ID: self[constants.CLIENT__ID],
            constants.CLIENT__NAME: self[constants.CLIENT__NAME],
            constants.CLIENT__PHONE_NUMBER: self[constants.CLIENT__PHONE_NUMBER],
            # constants.CLIENT__ASSIGNED_TO: self[constants.CLIENT__ASSIGNED_TO].fetch().name,
            constants.CREATED_ON: common_utils.epoch_to_datetime(self[constants.CREATED_ON]),
        }