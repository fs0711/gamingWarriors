# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils
from gwBackend.UserManagement.models.User import User

class Gameunit(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.GAMEUNIT__TYPE: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.GAMEUNIT__GAME_LEVEL: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.GAMEUNIT__PLAY_COUNT: [{"rule": "datatype", "datatype": str}],
            constants.GAMEUNIT__UNIT_STATUS: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.GAMEUNIT__GAME_STATUS: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.GAMEUNIT__BRANCH: [],
        }

    @classmethod
    def update_validation_rules(cls): 
        return {}

    type = db.StringField(required=True)
    branch = db.LazyReferenceField('Branch')
    game_level = db.StringField(reuired=True)
    play_count = db.StringField(required=True)
    unit_status = db.StringField(required=True)
    game_status = db.StringField(required=True)
    cost = db.IntField(required=True)

    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.GAMEUNIT__TYPE: self[constants.GAMEUNIT__TYPE],
            constants.GAMEUNIT__BRANCH: self[constants.GAMEUNIT__BRANCH],
            constants.GAMEUNIT__GAME_LEVEL: self[constants.GAMEUNIT__GAME_LEVEL],
            constants.GAMEUNIT__PLAY_COUNT: self[constants.GAMEUNIT__PLAY_COUNT],
            constants.GAMEUNIT__UNIT_STATUS: self[constants.GAMEUNIT__UNIT_STATUS],
            constants.GAMEUNIT__GAME_STATUS: self[constants.GAMEUNIT__GAME_STATUS],
            constants.GAMEUNIT__COST: self[constants.GAMEUNIT__COST],
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