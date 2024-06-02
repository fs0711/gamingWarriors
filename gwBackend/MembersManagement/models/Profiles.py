# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.MembersManagement.models.Members import Members
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
    card_id = db.LazyReferenceField("Cards")
    credit = db.IntField(required=True)
    reward = db.IntField(required=True)
    game_history = db.ObjectField()
    member_id = db.LazyReferenceField("Members")


    def __str__(self):
        return str(self.pk)

    def display(self):
        return {

        }

    def display_min(self):
        return {

        }