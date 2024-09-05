# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.UserManagement.models import User
from gwBackend.generic.services.utils import constants, common_utils

class Client(models.Model):
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
    
    
    name = db.StringField(required=True)
    organization = db.LazyReferenceField('Organization', required=True)
    contact_person = db.StringField(required=True)
    cp_phone_number = db.ListField()
    cp_email_address = db.StringField()
    country = db.StringField(required=True)
    city = db.StringField(required=True)
    zipcode = db.StringField(required=True)
    client_id = db.SequenceField(value_decorator='CL-{}'.format)
    
    
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