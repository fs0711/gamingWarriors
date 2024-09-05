# Date Created 14/09/2021 17:05:00


# Local imports
from gwBackend import app
from gwBackend.config import config
from gwBackend.generic.services.utils import common_utils, constants
from gwBackend.UserManagement.controllers.UserController import UserController
from gwBackend.RfCardManagement.controllers.RfCardController import RfCardController
from gwBackend.BranchManagement.controllers.BranchController import BranchController
from gwBackend.OrganizationsManagement.controllers.organizationcontroller import OrganizationController


def create_admin_user_if_not_exists(run=False):
    if not run:
        return
    with app.test_request_context():
        if not bool(UserController.db_read_records({}).count()):
            print("No Users")
            is_valid, error_messages, obj = BranchController.db_insert_record(
                data={
                    constants.BRANCH__NAME: config.DEFAULT_BRANCH_NAME,
                    constants.BRANCH__CITY:config.DEFAULT_BRANCH_CITY,
                    constants.BRANCH__OPENING_TIME:config.DEFAULT_BRANCH_OPENING_TIME,
                    constants.BRANCH__CLOSING_TIME:config.DEFAULT_BRANCH_CLOSING_TIME,
                    constants.BRANCH__GAME_TYPES:config.DEFAULT_BRANCH_GAME_TYPES
                }
            )
            branch_id = str(obj.id)

            is_valid, error_messages, obj = OrganizationController.db_insert_record(
                data={
                    constants.ORGANIZATION__NAME: config.DEFAULT_ADMIN_ORGANIZATION_NAME,
                    constants.ORGANIZATION__ADDRESS: config.DEFAULT_ADMIN_ADDRESS,
                    constants.ORGANIZATION__CITY: config.DEFAULT_ADMIN_CITY,
                    constants.ORGANIZATION__COUNTRY: config.DEFAULT_ADMIN_COUNTRY,
                    constants.ORGANIZATION__CP_NAME: config.DEFAULT_ADMIN_NAME,
                    constants.ORGANIZATION__CP_EMAIL: config.DEFAULT_ADMIN_EMAIL,
                    constants.ORGANIZATION__CP_PHONE_NUMBER: [config.DEFAULT_ADMIN_PHONE],
                    constants.ORGANIZATION__NTN: 'no ntn'
                })
            organization_id = str(obj.id)
            
            is_valid, error_messages, obj = RfCardController.db_insert_record(
                data={
                    constants.RFCARD__UID: config.DEFAULT_ADMIN_CARD_ID,
                    constants.RFCARD__ASSIGNED: "True",
                    constants.RFCARD__BRANCH: branch_id
                }
            )
            card_id = str(obj.id)

            is_valid, error_messages, obj = UserController.db_insert_record(
                data={
                    constants.USER__NAME: config.DEFAULT_ADMIN_NAME,
                    constants.USER__EMAIL_ADDRESS: config.DEFAULT_ADMIN_EMAIL,
                    constants.USER__PASSWORD:  common_utils.encrypt_password(password=config.DEFAULT_ADMIN_PASSWORD),
                    constants.USER__PHONE_NUMBER: config.DEFAULT_ADMIN_PHONE,
                    constants.USER__GENDER: constants.GENDER_LIST[0],
                    constants.USER__NIC: "123456",
                    constants.USER__ROLE: constants.DEFAULT_ADMIN_ROLE_OBJECT,
                    constants.USER__CITY: config.DEFAULT_ADMIN_CITY,
                    constants.USER__CARD_ID: card_id,
                    constants.USER__BRANCH: branch_id,
                    constants.USER__ORGANIZATION: organization_id
                }
            )
            if not is_valid:
                print(error_messages)
            print(obj.to_json())
