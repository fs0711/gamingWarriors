# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.AccountsManagement.controllers.AccountController import AccountsController
from gwBackend.AccountsManagement.models.Invoice import Invoice
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class InvoiceController(Controller):
    Model = Invoice

    @classmethod
    def create_controller(cls, data):
        obj = AccountsController.db_read_records(
            read_filter={constants.ID+"__in": data[constants.INVOICE__TRANSACTION]})
        user = common_utils.current_user()
        data[constants.INVOICE__CREATED_BY_ORGANIZATION] = str(
            user[constants.USER__ORGANIZATION].fetch().id)
        amount = 0.0
        transaction = []
        for item in obj:
            if user[constants.USER__ROLE][constants.USER__ROLE__ROLE_ID] == 1 or \
                    user[constants.USER__ROLE][constants.USER__ROLE__ROLE_ID] == 2:
                transaction.append(str(item[constants.ID]))
                amount += item[constants.ACCOUNTS__AMOUNT_ADMIN]
                update_data = {constants.ACCOUNTS__INVOICED: True}
            else:
                transaction.append(str(item[constants.ID]))
                amount += item[constants.ACCOUNTS__AMOUNT_ORGANIZATION]
                update_data = {constants.ACCOUNTS__INVOICED: True}
        data[constants.INVOICE__TRANSACTION] = transaction
        data[constants.INVOICE__AMOUNT] = amount
        data[constants.INVOICE__PAID] = False
        is_valid, validation_errors = cls.cls_validate_data(data=data)
        if not is_valid:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_VALIDATION_FAILED,
                response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                response_data=validation_errors
            )
        _, _, obj = cls.db_insert_record(data=data, db_commit=False)
        obj.save()
        is_valid, _, obj_acc = AccountsController.db_update_records(read_filter={constants.ID+"__in": transaction},
                                                   update_filter=update_data, default_validation=False)
        if is_valid:
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
    def pay_controller(cls, data):
        obj = cls.db_read_single_record(read_filter={constants.ID:data})
        obj[constants.INVOICE__PAID] = True
        obj.save()
        