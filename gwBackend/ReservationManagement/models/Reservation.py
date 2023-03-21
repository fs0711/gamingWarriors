# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils
from gwBackend.UserManagement.models.User import User

class Reservation(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.RESERVATION__GAME_ID: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.RESERVATION__CUSTOMER_ID: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.RESERVATION__TIME_SLOT: [{"rule": "datatype", "datatype": str}],
            constants.RESERVATION__RESV_STATUS: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
        }

    @classmethod
    def update_validation_rules(cls): 
        return {}

    game_id = db.StringField(required=True)
    customer_id = db.StringField(required=True)
    time_slot = db.StringField(reuired=True)
    resv_status = db.StringField(required=True)

    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.RESERVATION__CUSTOMER_ID: self[constants.RESERVATION__CUSTOMER_ID],
            constants.RESERVATION__GAME_ID: self[constants.RESERVATION__GAME_ID],
            constants.RESERVATION__TIME_SLOT: self[constants.RESERVATION__TIME_SLOT],
            constants.RESERVATION__RESV_STATUS: self[constants.RESERVATION__RESV_STATUS],
            constants.STATUS: self[constants.STATUS],
            constants.CREATED_BY: self.created_by.fetch().name,
            constants.CREATED_ON: self[constants.CREATED_ON],
            constants.UPDATED_ON: self[constants.UPDATED_ON],
        }

    def display_min(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.CREATED_ON: common_utils.epoch_to_datetime(self[constants.CREATED_ON]),
        }