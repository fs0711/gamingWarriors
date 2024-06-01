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

    member_id = db.SequenceField(value_decorator='MI-{}'.format)
    name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    email_address = db.StringField(reuired=True)
    city = db.StringField(required=True)
    nic = db.StringField()
    profiles = db.ListField(required=True)
    membership_level = db.IntField(required=True)


    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
        }

    def display_min(self):
        return {
        }