# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.AccountsManagement.models.Account import Accounts
from gwBackend.MembersManagement.controllers.MemberController import MemberController
from gwBackend.BranchManagement.controllers.BranchController import BranchController
from gwBackend.RfCardManagement.controllers.RfCardController import RfCardController
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class AccountsController(Controller):
    Model = Accounts

    @classmethod
    def create_controller(cls, data):
        data[constants.ACCOUNTS__TYPE] = "credit"
        card = RfCardController.read_UID_controller(data=data[constants.MEMBER__CARD_ID])
        # card = RfCardController.db_read_single_record(read_filter={constants.data[constants.MEMBER__CARD_ID])
        card_id = str(card[constants.ID])
        user = common_utils.current_user()
        if data[constants.ACCOUNTS__AMOUNT] != "0":
            # card_id = RfCardController.read_UID_controller(data=data[constants.MEMBER__CARD_ID])
            if card_id:
                data[constants.ACCOUNTS__ORGANIZATION] = str(card[constants.USER__ORGANIZATION].fetch().id)
                data[constants.ACCOUNTS__ORGANIZATION_NAME] = str(card[constants.USER__ORGANIZATION].fetch().name)
                data[constants.ACCOUNTS__BRANCH] = str(card[constants.USER__BRANCH].fetch().id)
                credit_limit = card[constants.USER__BRANCH].fetch().credit_limit
                branch_percentage = card[constants.USER__BRANCH].fetch().percentage
                org_percentage = card[constants.USER__ORGANIZATION].fetch().percentage
                if credit_limit - data[constants.ACCOUNTS__AMOUNT] >= 0:
                    if data[constants.ACCOUNTS__PURPOSE] == constants.PAYMENT_PURPOSE[0]:
                        obj = MemberController.recharge_controller(data={constants.MEMBER__CARD_ID: card_id, 
                                                                    constants.ACCOUNTS__AMOUNT:data[constants.ACCOUNTS__AMOUNT]})
                        if obj["status"] != 1:
                            return response_utils.get_response_object(
                                response_code=response_codes.CODE_WRONG_PARAMETERS,
                                response_message=response_codes.MESSAGE_GENERAL_ERROR
                            )
                        else:
                            data[constants.ACCOUNTS__MEMBER_ID] = obj["id"]
                            obj = BranchController.update_limit(data = {constants.ID: data[constants.ACCOUNTS__BRANCH],
                                                                         constants.BRANCH__CREDIT_LIMIT: credit_limit - data[constants.ACCOUNTS__AMOUNT]})
                            del data[constants.MEMBER__CARD_ID]
                            data[constants.ACCOUNTS__AMOUNT_ORGANIZATION] = data[constants.ACCOUNTS__AMOUNT] * (branch_percentage / 100)
                            data[constants.ACCOUNTS__AMOUNT_ADMIN] = data[constants.ACCOUNTS__AMOUNT] * (org_percentage / 100)
                            data[constants.ACCOUNTS__PAID_ADMIN] = False
                            data[constants.ACCOUNTS__PAID_ORGANIZATION] = False
                            data[constants.ACCOUNTS__INVOICED] = False
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
                    else:
                         return response_utils.get_response_object(
                            response_code=response_codes.CODE_WRONG_PARAMETERS,
                            response_message=response_codes.MESSAGE_WRONG_PURPOSE
                         )
                else:
                    return response_utils.get_response_object(
                        response_code=response_codes.CODE_WRONG_PARAMETERS,
                        response_message=response_codes.MESSAGE_WRONG_CREDIT_LIMIT
                    )
            else:
                return response_utils.get_response_object(
                    response_code=response_codes.CODE_WRONG_PARAMETERS,
                    response_message=response_codes.MESSAGE_WRONG_CARD_ID
                )
        else:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_WRONG_PARAMETERS,
                response_message=response_codes.MESSAGE_WRONG_AMOUNT
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
    def list_controller(cls, data):
            obj = cls.db_read_records(read_filter={constants.ORGANIZATION:data[constants.ORGANIZATION],constants.BRANCH:data[constants.BRANCH],constants.CREATED_ON + "__gte" :data[constants.ACCOUNTS__START_DATE],constants.CREATED_ON + "__lte" :data[constants.ACCOUNTS__END_DATE]})
            list = [acc.display() for acc in obj]
            return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data= list)