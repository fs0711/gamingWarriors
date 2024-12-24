# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.AccountsManagement.models.Accounts import Accounts
from gwBackend.MembersManagement.controllers.MembersController import MembersController
from gwBackend.AccountsManagement.controllers.ProfitController import ProfitController
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
            amount_org = amount * percentage
            amount_admin = amount * (1.0 - percentage)

            
            is_valid, error_messages, obj = ProfitController.db_insert_record(
                data={
                    constants.PROFIT__AMOUNT_ADMIN: amount_admin,
                    constants.PROFIT__AMOUNT_ORGANIZATION: amount_org,
                    constants.PROFIT__TOTAL_AMOUNT : amount,
                    constants.PROFIT__ORGANIZATION: str(user[constants.USER__ORGANIZATION].fetch().id),
                }
            )
            
            if amount_org != "0":
                obj = OrganizationController.sales_controller(data={constants.ACCOUNTS__ORGANIZATION_NAME: data[constants.ACCOUNTS__ORGANIZATION_NAME], 
                                                         constants.ACCOUNTS__AMOUNT:amount_org})
        
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
                
    @classmethod
    def read_UID_controller(cls, data):
        obj = cls.db_read_single_record(read_filter={constants.RFCARD__UID:data})
        if obj:    
            return str(obj.id)
        else:
            return 0
        
    @classmethod
    def get_transactions(cls):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[{'transaction_id':obj[constants.ACCOUNTS__ID],'amount':obj[constants.ACCOUNTS__AMOUNT],'purpose':obj[constants.ACCOUNTS__PURPOSE],'type':obj[constants.ACCOUNTS__TYPE],'branch':str(obj[constants.ACCOUNTS__BRANCH].fetch().name),'organization':str(obj[constants.ACCOUNTS__ORGANIZATION].fetch().name)  } for obj in cls.db_read_records(read_filter={})],
        )

# , 'member':str(obj[constants.ACCOUNTS__MEMBER_ID].fetch().member_id)
    # @classmethod
    # def update_controller(cls, data):
    #     is_valid, error_messages, obj = cls.db_update_single_record(
    #         read_filter={constants.ID: data[constants.ID]}, update_filter=data
    #     )
    #     if not is_valid:
    #         return response_utils.get_response_object(
    #             response_code=response_codes.CODE_VALIDATION_FAILED,
    #             response_message=response_codes.MESSAGE_VALIDATION_FAILED,
    #             response_data=error_messages
    #         )
    #     if not obj:
    #         return response_utils.get_response_object(
    #             response_code=response_codes.CODE_RECORD_NOT_FOUND,
    #             response_message=response_codes.MESSAGE_NOT_FOUND_DATA.format(
    #                 constants.CLIENT.title(), constants.ID
    #             ))
    #     return response_utils.get_response_object(
    #         response_code=response_codes.CODE_SUCCESS,
    #         response_message=response_codes.MESSAGE_SUCCESS,
    #         response_data=obj.display(),
    #     )

    # @classmethod
    # def suspend_controller(cls, data):
    #     _, _, obj = cls.db_update_single_record(
    #         read_filter={constants.ID: data[constants.ID]},
    #         update_filter={
    #             constants.STATUS: constants.OBJECT_STATUS_SUSPENDED},
    #         update_mode=constants.UPDATE_MODE__PARTIAL,
    #     )
    #     if obj:
    #         return response_utils.get_response_object(
    #             response_code=response_codes.CODE_SUCCESS,
    #             response_message=response_codes.MESSAGE_SUCCESS,
    #             response_data=obj.display(),
    #         )
    #     return response_utils.get_response_object(
    #         response_code=response_codes.CODE_RECORD_NOT_FOUND,
    #         response_message=response_codes.MESSAGE_NOT_FOUND_DATA.format(
    #             constants.GAMEUNIT.title(), constants.ID
    #         ))
        
    # @classmethod
    # def get_rfcards(cls,data):
    #     return response_utils.get_json_response_object(
    #     response_code=response_codes.CODE_SUCCESS,
    #     response_message=response_codes.MESSAGE_SUCCESS,
    #     response_data=[obj.display_min() for obj in cls.db_read_records(read_filter=data)],
    #     )
