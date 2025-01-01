# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.AccountsManagement.models.Accounts import Accounts
from gwBackend.MembersManagement.controllers.MembersController import MembersController
from gwBackend.OrganizationsManagement.controllers.organizationcontroller import OrganizationController
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class AccountsController(Controller):
    Model = Accounts

    @classmethod
    def create_controller(cls, data):
        data[constants.ACCOUNTS__TYPE] = "credit"
        user = common_utils.current_user()
        data[constants.ACCOUNTS__ORGANIZATION] = str(user[constants.USER__ORGANIZATION].fetch().id)
        data[constants.ACCOUNTS__ORGANIZATION_NAME] = str(user[constants.USER__ORGANIZATION].fetch().name)
        data[constants.ACCOUNTS__BRANCH] = str(user[constants.USER__BRANCH].fetch().id)
        if data[constants.ACCOUNTS__PURPOSE] == "card_recharge":
            obj = MembersController.recharge_controller(data={constants.MEMBER__CARD_ID: data[constants.MEMBER__CARD_ID], 
                                                         constants.ACCOUNTS__AMOUNT:data[constants.ACCOUNTS__AMOUNT]})
            data[constants.ACCOUNTS__TYPE] = "card_recharge"
            if obj["status"] != 1:
                return response_utils.get_response_object(
                    response_code=response_codes.CODE_WRONG_PARAMETERS,
                    response_message=response_codes.MESSAGE_GENERAL_ERROR
                )
        if data[constants.ACCOUNTS__AMOUNT] != "0":
            amount = float(data[constants.ACCOUNTS__AMOUNT])
            percentage =  float(user[constants.USER__ORGANIZATION].fetch().profit)
            data[constants.ACCOUNTS__AMOUNT_ORGANIZATION] = amount * percentage
            data[constants.ACCOUNTS__AMOUNT_ADMIN] = amount * (1.0 - percentage)

            if data[constants.ACCOUNTS__AMOUNT_ORGANIZATION] != "0":
                obj = OrganizationController.sales_controller(data={constants.ACCOUNTS__ORGANIZATION_NAME: data[constants.ACCOUNTS__ORGANIZATION_NAME], 
                                                         constants.ACCOUNTS__AMOUNT:data[constants.ACCOUNTS__AMOUNT_ORGANIZATION] })
                
            
            admin_organization_name = "MUNAS"
            if data[constants.ACCOUNTS__AMOUNT_ADMIN] != "0":
                obj = OrganizationController.sales_controller(data={constants.ACCOUNTS__ORGANIZATION_NAME: admin_organization_name, 
                                                         constants.ACCOUNTS__AMOUNT:data[constants.ACCOUNTS__AMOUNT_ADMIN]})
         
        del data[constants.MEMBER__CARD_ID]
        is_valid, error_messages = cls.cls_validate_data(data=data)
        if not is_valid:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_VALIDATION_FAILED,
                response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                response_data=error_messages
            )
        else:
            _,_,obj = cls.db_insert_record(data=data, db_commit=False)
            obj.save()
            return response_utils.get_response_object(
                response_code=response_codes.CODE_SUCCESS,
                response_message=response_codes.MESSAGE_SUCCESS,
                response_data=obj.display()
            )


    @classmethod
    def read_controller(cls, data):
                return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data=[
                obj.display() for obj in cls.db_read_records(read_filter=data)
            ])