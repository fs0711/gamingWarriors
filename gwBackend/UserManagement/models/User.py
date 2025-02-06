# Python imports

# Framework imports

# Local imports
from gwBackend.generic import models
from gwBackend.generic import db
from gwBackend.generic.services.utils import common_utils, constants


class User(models.Model):
    @classmethod
    def validation_rules(cls):
        return {
            constants.USER__NAME: [
                {"rule": "datatype", "datatype": str},
            ],
            constants.USER__EMAIL_ADDRESS: [
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.USER__EMAIL_ADDRESS,
                },
            ],
            constants.USER__PHONE_NUMBER: [
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.USER__PHONE_NUMBER,
                },
            ],
            constants.USER__PASSWORD: [
                {"rule": "datatype", "datatype": str},
                {"rule": "password"},
            ],
            constants.USER__GENDER: [
                {"rule": "choices", "options": constants.GENDER_LIST},
            ],
            constants.USER__ROLE: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": dict},
                {"rule": "choices", "options": constants.DEFAULT_ROLE_OBJECTS},
            ],
            constants.USER__MANAGER: [],
        }

    @classmethod
    def login_validation_rules(cls):
        return {
            constants.USER__EMAIL_ADDRESS: [
                {"rule": "datatype", "datatype": str},
            ],
            constants.USER__PASSWORD: [
                {"rule": "datatype", "datatype": str},
                {"rule": "password"},
            ],
        }

    @classmethod
    def update_validation_rules(cls):
        return {
            constants.USER__ROLE: [
                {"rule": "non-existent"},
            ],
        }

    name = db.StringField()
    email_address = db.StringField()
    phone_number = db.StringField()
    password = db.StringField()
    gender = db.StringField()
    card_id=db.LazyReferenceField(document_type="RfCard")
    city=db.StringField()
    role = db.DictField(required=True)
    nic = db.StringField()
    url_key = db.StringField(default = "")
    manager = db.LazyReferenceField(document_type="User")
    organization = db.LazyReferenceField(document_type="Organization")
    branch = db.LazyReferenceField(document_type="Branch")
    
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.USER__NAME: self[constants.USER__NAME],
            constants.USER__CARD_ID: self[constants.USER__CARD_ID].fetch().card_id,
            constants.USER__BRANCH: str(self[constants.USER__BRANCH].fetch().id) if self[constants.USER__BRANCH] else "",
            constants.USER__ORGANIZATION: str(self[constants.USER__ORGANIZATION].fetch().id),
            constants.USER__CITY: self[constants.USER__CITY],
            constants.USER__EMAIL_ADDRESS: self[constants.USER__EMAIL_ADDRESS],
            constants.USER__PHONE_NUMBER: self[constants.USER__PHONE_NUMBER],
            constants.USER__GENDER: self[constants.USER__GENDER],
            constants.USER__ROLE: self[constants.USER__ROLE],
            constants.STATUS: self[constants.STATUS],
        }

    def display_id(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.USER__NAME: self[constants.USER__NAME]
        }

    def display_user_list(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.USER__NAME: self[constants.USER__NAME],   
            constants.USER__BRANCH: str(self[constants.USER__BRANCH].fetch().id) if self[constants.USER__BRANCH] else "",
            constants.USER__ORGANIZATION: str(self[constants.USER__ORGANIZATION].fetch().id),
            constants.USER__EMAIL_ADDRESS: self[constants.USER__EMAIL_ADDRESS],
            constants.USER__PHONE_NUMBER: self[constants.USER__PHONE_NUMBER],   
        }

    def verify_password(self, password):
        return common_utils.verify_password(self.password, password)
