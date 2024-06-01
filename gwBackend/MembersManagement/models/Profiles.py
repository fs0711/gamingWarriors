# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils

class Profiles(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
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