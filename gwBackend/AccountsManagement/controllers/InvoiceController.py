# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.AccountsManagement.models.Invoice import Invoice
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class InvoiceController(Controller):
    Model = Invoice

    @classmethod
    def create_controller(cls, data):
        




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