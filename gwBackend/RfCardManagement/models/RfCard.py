# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.BranchManagement.models.Branch import Branch
from gwBackend.generic.services.utils import constants, common_utils


class RfCard(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.RFCARD__UID: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.RFCARD__UID,
                },
                {"rule":"length", "length":8},
            ]
        }

    @classmethod
    def update_validation_rules(cls): 
        return {}

    card_id = db.SequenceField(value_decorator='CI-{}'.format)
    card_uid = db.StringField(required=True)
    branch = db.LazyReferenceField('Branch')
    assigned = db.BooleanField(Default = False)

    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.RFCARD__UID: self[constants.RFCARD__UID],
            constants.RFCARD__ASSIGNED: self[constants.RFCARD__ASSIGNED],
            constants.RFCARD__BRANCH:self [constants.RFCARD__BRANCH].fetch().name
        }

    def display_min(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.CREATED_ON: common_utils.epoch_to_datetime(self[constants.CREATED_ON]),
        }