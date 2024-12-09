# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.RfCardManagement.models.RfCard import RfCard
from gwBackend.generic.services.utils import constants, common_utils
from gwBackend.UserManagement.models.User import User

class Members(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.MEMBER__NAME: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.MEMBER__NIC: [{"rule": "datatype", "datatype": str}],
            constants.MEMBER__CARD_ID: [{"rule": "datatype", "datatype": str}],
            # constants.MEMBER__PARENT: [{"rule": "datatype", "datatype": str}],
            constants.MEMBER__MEMBERSHIP_LEVEL: [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
            constants.MEMBER__REWARD : [{"rule": "datatype", "datatype": str}],
            constants.MEMBER__CREDIT : [{"rule": "required"}, {"rule": "datatype", "datatype": int}],
            constants.MEMBER__TYPE : [{"rule": "datatype", "datatype": str}],

        }

    @classmethod
    def update_validation_rules(cls): return {

    }

    member_id = db.SequenceField(value_decorator='MI-{}'.format)
    name = db.StringField(required=True)
    nic = db.StringField()
    membership_level = db.StringField(required=True)
    reward = db.StringField(required=True)
    game_history = db.DictField(default = {})
    credit = db.IntField(required=True)
    type = db.StringField(required=True)
    parent = db.LazyReferenceField(document_type="Members")
    card_id = db.LazyReferenceField(document_type="RfCard")
    organization_id = db.LazyReferenceField(document_type="Organization")
    user_id = db.LazyReferenceField(document_type="User")


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
            constants.MEMBER__ID:self[constants.MEMBER__ID],
            constants.MEMBER__REWARD:self[constants.MEMBER__REWARD],
            constants.MEMBER__GAME_HISTORY:self[constants.MEMBER__GAME_HISTORY],
            constants.MEMBER__CREDIT:self[constants.MEMBER__CREDIT],
            constants.MEMBER__TYPE:self[constants.MEMBER__TYPE],
            constants.MEMBER__PARENT:str(self[constants.MEMBER__PARENT].fetch().name),
            constants.MEMBER__ORGANIZATION_ID:str(self[constants.MEMBER__ORGANIZATION_ID].fetch().id)
            # constants.MEMBER__CARD_ID:self[constants.MEMBER__CARD_ID].fetch().card_id
        }

    def display_min(self):
        return {
        }