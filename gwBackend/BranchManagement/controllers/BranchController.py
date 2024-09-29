# Python imports

# Framework imports

# Local imports
from gwBackend import config
from gwBackend.BranchManagement.models.Branch import Branch
from gwBackend.generic.controllers import Controller
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils


class BranchController(Controller):
    Model = Branch

    @classmethod
    def create_controller(cls, data):
        is_valid, error_messages, obj = cls.db_insert_record(
            data=data, db_commit=False)
        if is_valid:
            obj.save()
            return response_utils.get_response_object(
                response_code=response_codes.CODE_SUCCESS,
                response_message=response_codes.MESSAGE_SUCCESS,
                response_data=obj.display()
            )
        return response_utils.get_response_object(
            response_code=response_codes.CODE_VALIDATION_FAILED,
            response_message=response_codes.MESSAGE_VALIDATION_FAILED,
            response_data=error_messages
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
    def update_controller(cls, data):
        is_valid, error_messages, obj = cls.db_update_single_record(
            read_filter={constants.ID: data[constants.ID]}, update_filter=data
        )
        if not is_valid:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_VALIDATION_FAILED,
                response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                response_data=error_messages
            )
        if not obj:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_RECORD_NOT_FOUND,
                response_message=response_codes.MESSAGE_NOT_FOUND_DATA.format(
                    constants.USER.title(), constants.ID
                ))
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data=obj.display(),
        )

    @classmethod
    def suspend_controller(cls, data):
        _, _, obj = cls.db_update_single_record(
            read_filter={constants.ID: data[constants.ID]},
            update_filter={
                constants.STATUS: constants.OBJECT_STATUS_SUSPENDED},
            update_mode=constants.UPDATE_MODE__PARTIAL,
        )
        if obj:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_SUCCESS,
                response_message=response_codes.MESSAGE_SUCCESS,
                response_data=obj.display(),
            )
        return response_utils.get_response_object(
            response_code=response_codes.CODE_RECORD_NOT_FOUND,
            response_message=response_codes.MESSAGE_NOT_FOUND_DATA.format(
                constants.USER.title(), constants.ID
            ))
        
    @classmethod
    def get_branchs(cls):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[{'branch_id':obj[constants.BRANCH__ID], 'name':obj[constants.BRANCH__NAME],'city':obj[constants.BRANCH__CITY],'opening_time':obj[constants.BRANCH__OPENING_TIME],'closing_time':obj[constants.BRANCH__CLOSING_TIME],'organization':str(obj[constants.BRANCH__ORGANIZATION].fetch().name)  } for obj in cls.db_read_records(read_filter={})],
        )
        
    @classmethod
    def get_branchs_ids(cls):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[{'id':str(obj[constants.ID]), 'name':obj[constants.BRANCH__NAME],'organization':str(obj[constants.BRANCH__ORGANIZATION].fetch().id) } for obj in cls.db_read_records(read_filter={})],
        )
    

        
    @classmethod
    def get_branchs_orgs(cls,data):
        
        obj = cls.db_read_records(read_filter={constants.BRANCH__ORGANIZATION:data[constants.BRANCH__ORGANIZATION]})
        branch_id_list = [branch.display_branchs_id() for branch in obj]
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=branch_id_list
        )
