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
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
            ],
            constants.USER__EMAIL_ADDRESS: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.USER__EMAIL_ADDRESS,
                },
            ],
            constants.USER__PHONE_NUMBER: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.USER__PHONE_NUMBER,
                },
            ],
            constants.USER__PASSWORD: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {"rule": "password"},
            ],
            constants.USER__GENDER: [
                {"rule": "required"},
                {"rule": "choices", "options": constants.GENDER_LIST},
            ],
            constants.USER__NIC: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {
                    "rule": "unique",
                    "Model": cls,
                    "Field": constants.USER__NIC,
                },
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
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
            ],
            constants.USER__PASSWORD: [
                {"rule": "required"},
                {"rule": "datatype", "datatype": str},
                {"rule": "password"},
            ],
        }

    @classmethod
    def update_validation_rules(cls):
        return {}

    name = db.StringField(required=True)
    address = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    nic = db.StringField(required=True)
<<<<<<< HEAD
    card_id=db.StringField(required=True)
    city=db.StringField(required=True)
    role = db.DictField(required=True)
    manager = db.LazyReferenceField('User')
=======
    password = db.StringField(required=True)
    branch = db.StringField(required=True)
    email_address = db.DictField(required=True)
    # manager = db.LazyReferenceField('User')
>>>>>>> 86418a004044ce20cf2fc72ce82eef63b06c511f
    def __str__(self):
        return str(self.pk)

    def display(self):
        return {
            constants.ID: str(self[constants.ID]),
            constants.USER__NAME: self[constants.USER__NAME],
<<<<<<< HEAD
            constants.USER__CARD_ID: self[constants.USER__CARD_ID],
            constants.USER__CITY: self[constants.USER__CITY],
            constants.USER__EMAIL_ADDRESS: self[constants.USER__EMAIL_ADDRESS],
=======
            # constants.USER__ADDRESS: self[constants.USER__ADDRESS],
>>>>>>> 86418a004044ce20cf2fc72ce82eef63b06c511f
            constants.USER__PHONE_NUMBER: self[constants.USER__PHONE_NUMBER],
            constants.USER__NIC: self[constants.USER__NIC],
            constants.USER__PASSWORD: self[constants.USER__PASSWORD],
            # constants.USER__BRANCH: self[constants.USER__BRANCH],
            constants.STATUS: self[constants.STATUS],
        }

    def verify_password(self, password):
        return common_utils.verify_password(self.password, password)
