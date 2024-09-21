# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils


class Accounts(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.ACCOUNTS__AMOUNT: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": int}
            ],
            constants.ACCOUNTS__PURPOSE: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str}
            ]
        }

    @classmethod
    def update_validation_rules(cls): 
        return {}

    transaction_id = db.SequenceField(value_decorator='TI-{}'.format)
    type = db.StringField(required=True)
    branch = db.LazyReferenceField('Branch')
    organization = db.LazyReferenceField('Organization')
    amount = db.IntField(required=True)
    member = db.LazyReferenceField('Members')
    purpose = db.StringField(required=True)
    

    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.ACCOUNTS__ID: self[constants.ACCOUNTS__ID],
            constants.ACCOUNTS__BRANCH:self[constants.ACCOUNTS__BRANCH].fetch().name,
            constants.ACCOUNTS__ORGANIZATION:self [constants.ACCOUNTS__ORGANIZATION].fetch().name,
            constants.ACCOUNTS__MEMBER_ID:self [constants.ACCOUNTS__MEMBER_ID].fetch().name if self[constants.ACCOUNTS__MEMBER_ID] else "",
            constants.ACCOUNTS__AMOUNT: self[constants.ACCOUNTS__AMOUNT],
            constants.ACCOUNTS__PURPOSE: self[constants.ACCOUNTS__PURPOSE],
            
        }
