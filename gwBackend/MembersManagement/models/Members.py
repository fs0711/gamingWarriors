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
            constants.MEMBER__NAME: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.MEMBER__NIC: [{"rule": "datatype", "datatype": str}],
            constants.MEMBER__PHONE_NUMBER: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.MEMBER__PHONE_NUMBER,
                },
            ],
            constants.MEMBER__EMAIL_ADDRESS: [{"rule": "email"}, {"rule": "datatype", "datatype": str}],
            constants.MEMBER__CARD_UID: [{"rule": "datatype", "datatype": str}],
            constants.MEMBER__MEMBERSHIP_LEVEL: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.MEMBER__CITY: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
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
            constants.ID: str(self[constants.ID]),
            constants.MEMBER__NAME:self[constants.MEMBER__NAME],
            constants.MEMBER__PHONE_NUMBER:self[constants.MEMBER__PHONE_NUMBER],
            constants.MEMBER__EMAIL_ADDRESS:self[constants.MEMBER__EMAIL_ADDRESS],
            constants.MEMBER__CITY:self[constants.MEMBER__CITY],
            constants.MEMBER__MEMBERSHIP_LEVEL:self[constants.MEMBER__MEMBERSHIP_LEVEL],
            constants.MEMBER__PROFILES:self[constants.MEMBER__PROFILES],
            constants.MEMBER__ID:self[constants.MEMBER__ID]
        }

    def display_min(self):
        return {
        }