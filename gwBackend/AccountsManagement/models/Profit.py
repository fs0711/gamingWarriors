# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.UserManagement.models import User
from gwBackend.generic.services.utils import constants, common_utils

class Profit(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.PROFIT__AMOUNT_ORGANIZATION: [{"rule": "required"}, {"rule": "datatype", "datatype": float}],
            constants.PROFIT__AMOUNT_ADMIN: [{"rule": "required"}, {"rule": "datatype", "datatype": float}],
            constants.PROFIT__TOTAL_AMOUNT: [{"rule": "required"}, {"rule": "datatype", "datatype": float}],
        }

    @classmethod
    def update_validation_rules(cls): return {
    }
    
    
    profit_id = db.SequenceField(value_decorator='PR-{}'.format)
    profit_org = db.FloatField(required=True)
    profit_admin = db.FloatField(required=True)
    total_amount = db.FloatField(required=True)
    organization = db.LazyReferenceField("Organization")
    
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.PROFIT__ID: self[constants.PROFIT__ID],
            constants.PROFIT__AMOUNT_ORGANIZATION: self[constants.PROFIT__AMOUNT_ORGANIZATION],
            constants.PROFIT__AMOUNT_ADMIN: self[constants.PROFIT__AMOUNT_ADMIN],
            constants.PROFIT__TOTAL_AMOUNT: self[constants.PROFIT__TOTAL_AMOUNT],
            
            #constants.BRANCH__ORGANIZATION: self[constants.BRANCH__ORGANIZATION].fetch().name,
            constants.STATUS: self[constants.STATUS],
        }
    
   