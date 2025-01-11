# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import constants, common_utils


class Invoice(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.INVOICE__AMOUNT: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": float}
            ],
            constants.INVOICE__TRANSACTION:[
                {"rule": "required"},
                {"rule": "datatype", "datatype": list}
            ],
            constants.INVOICE__BRANCH:[
                {"rule": "datatype", "datatype": str}
            ],
            constants.INVOICE__ORGANIZATION:[
                {"rule": "datatype", "datatype": str}
            ],
            constants.INVOICE__PAID:[
                {"rule": "required"},
                {"rule": "datatype", "datatype": bool}
            ],
            constants.INVOICE__CREATED_BY_ORGANIZATION:[
                {"rule": "required"},
                {"rule": "datatype", "datatype": str}
            ]
        }

    @classmethod
    def update_validation_rules(cls): 
        return {
            constants.INVOICE__AMOUNT: [{"rule":"non-existent"}],
            constants.INVOICE__BRANCH: [{"rule":"non-existent"}],
            constants.INVOICE__ORGANIZATION: [{"rule":"non-existent"}],
            constants.INVOICE__CREATED_BY_ORGANIZATION: [{"rule":"non-existent"}],
            constants.INVOICE__PAID: [{"rule":"non-existent"}],
            constants.INVOICE__TRANSACTION: [{"rule":"non-existent"}]
        }

    invoice_id = db.SequenceField(value_decorator='DZ-{}'.format)
    organization = db.LazyReferenceField(document_type="Organization")
    branch = db.LazyReferenceField(document_type="Branch")
    created_by_organization = db.LazyReferenceField(document_type="Organization")
    amount = db.FloatField(required=True)
    paid = db.BooleanField(required=True)
    transaction = db.ListField(required=True)    
    
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.INVOICE__ID: self[constants.INVOICE__ID],
            constants.INVOICE__BRANCH:self[constants.INVOICE__BRANCH].fetch().name if self[constants.INVOICE__BRANCH] else "",
            constants.INVOICE__ORGANIZATION:self [constants.INVOICE__ORGANIZATION].fetch().name if self[constants.INVOICE__ORGANIZATION] else "",
            constants.INVOICE__AMOUNT: self[constants.INVOICE__AMOUNT],
            constants.INVOICE__PAID: self[constants.INVOICE__PAID],
            constants.INVOICE__TRANSACTION: self[constants.INVOICE__TRANSACTION]
        }
