# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.MembersManagement.models.Members import Members
from gwBackend.RfCardManagement.models.RfCard import RfCard
from gwBackend.generic.services.utils import constants, common_utils

class Profiles(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
        }

    @classmethod
    def update_validation_rules(cls): return {

    }

    name = db.StringField(required=True)
    card_id = db.LazyReferenceField("RfCard")
    credit = db.IntField(required=True)
    reward = db.IntField(required=True)
    game_history = db.DictField(default = {})
    member_id = db.LazyReferenceField("Members")


    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.PROFILE__NAME:self[constants.PROFILE__NAME],
            constants.PROFILE__CARD_ID:self[constants.PROFILE__CARD_ID].fetch().id,
            constants.PROFILE__CREDIT:self[constants.PROFILE__CREDIT],
            constants.PROFILE__REWARD:self[constants.PROFILE__REWARD],
            constants.PROFILE__MEMBER_ID:self[constants.PROFILE__MEMBER_ID].fetch().id
        }

    def display_min(self):
        return {

        }