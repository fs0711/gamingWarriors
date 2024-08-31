# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.UserManagement.models import User
from gwBackend.generic.services.utils import constants, common_utils

class Branch(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.BRANCH__NAME: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.BRANCH__CITY: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.BRANCH__LOCATION_LNG: [{"rule": "datatype", "datatype": float}],
            constants.BRANCH__LOCATION_LAT: [{"rule": "datatype", "datatype": float}],
            constants.BRANCH__GAME_TYPES: [{"rule": "datatype", "datatype": list},
                                           {"rule": "collection_format", "datatype": list,
                                           "validation_rules": [{"rule": "required"}]}],        
            constants.BRANCH__USERS: [{"rule": "datatype", "datatype": str},{"rule": "required"}],
            constants.BRANCH__OPENING_TIME: [{"rule": "required"}],
            constants.BRANCH__CLOSING_TIME: [{"rule": "required"}],
        }

    @classmethod
    def update_validation_rules(cls): return {
            constants.BRANCH__NAME: [{"rule": "existent"}],
            constants.BRANCH__CITY: [{"rule": "existent"}],
            constants.BRANCH__OPENING_TIME: [{"rule": "existent"}],
            constants.BRANCH__CLOSING_TIME: [{"rule": "existent"}],
    }
    
    
    branch_id = db.SequenceField(value_decorator='BR-{}'.format)
    name = db.StringField(required=True)
    location_lng = db.FloatField()
    location_lat = db.FloatField()
    city = db.StringField(required=True)
    game_types = db.ListField()
    opening_time = db.IntField(required=True)
    closing_time = db.IntField(required=True)
    users = db.LazyReferenceField("User")
    
    
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.BRANCH__ID: self[constants.BRANCH__ID],
            constants.BRANCH__NAME: self[constants.BRANCH__NAME],
            constants.BRANCH__CITY: self[constants.BRANCH__CITY],
            constants.BRANCH__GAME_TYPES: self[constants.BRANCH__GAME_TYPES],
            constants.BRANCH__USERS: self[constants.BRANCH__USERS].fetch().name,
            constants.BRANCH__OPENING_TIME: self[constants.BRANCH__OPENING_TIME],
            constants.BRANCH__CLOSING_TIME: self[constants.BRANCH__CLOSING_TIME],
            constants.STATUS: self[constants.STATUS],
        }