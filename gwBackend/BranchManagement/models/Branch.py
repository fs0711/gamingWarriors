# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils

class Branch(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.BRANCH__NAME: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.BRANCH__CITY: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.BRANCH__LOCATION: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.BRANCH__GAME_TYPES: [{"rule": "datatype", "datatype": list},
                                           {"rule": "collection_format", "datatype": list,
                                            "validation_rules": [{"rule": "required"}, {"rule": "game_types"}]}],        
            constants.BRANCH__GAME_COUNT: [{"rule": "datatype", "datatype": list},
                                           {"rule": "collection_format", "datatype": list,
                                            "validation_rules": [{"rule": "required"}, {"rule": "game_count"}]}],
            constants.BRANCH__USERS: [{"rule": "datatype", "datatype": list},
                                           {"rule": "collection_format", "datatype": list,
                                            "validation_rules": [{"rule": "required"}, {"rule": "users"}]}],
            constants.BRANCH__OPENING_TIME: [{"rule": "required"}, {"rule": "datatype", "datatype": datetime}],
            constants.BRANCH__CLOSING_TIME: [{"rule": "required"}, {"rule": "datatype", "datatype": datetime}],
        }

    @classmethod
    def update_validation_rules(cls): return {

    }

    name = db.StringField(required=True)
    location = db.StringField()
    city = db.StringField()
    game_types = db.ListField()
    game_count = db.ListField()
    users = db.ListField()
    opening_time = db.DateTimeField(required=True)
    closing_time = db.DateTimeField(required=True)
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.BRANCH__ID: self[constants.BRANCH__ID],
            constants.BRANCH__NAME: self[constants.BRANCH__NAME],
            constants.BRANCH__LOCATION: self[constants.BRANCH__LOCATION],
            constants.BRANCH__CITY: self[constants.BRANCH__CITY],
            constants.BRANCH__GAME_TYPES: self[constants.BRANCH__GAME_TYPES],
            constants.BRANCH__GAME_COUNT: self[constants.BRANCH__GAME_COUNT],
            constants.BRANCH__USERS: self[constants.BRANCH__USERS],
            constants.BRANCH__OPENING_TIME: self[constants.BRANCH__OPENING_TIME],
            constants.BRANCH__CLOSING_TIME: self[constants.BRANCH__CLOSING_TIME],
            constants.STATUS: self[constants.STATUS],
        }