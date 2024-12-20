# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.RfCardManagement.models.RfCard import RfCard
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class RfCardController(Controller):
    Model = RfCard

    @classmethod
    def create_controller(cls, data):
        is_valid, error_messages = cls.cls_validate_data(data=data)
        if not is_valid:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_VALIDATION_FAILED,
                response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                response_data=error_messages
            )
        # current_user = common_utils.current_user()
        already_exists = cls.db_read_records(read_filter={
            constants.RFCARD__UID: data[constants.RFCARD__UID]
        })
        if already_exists:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_USER_ALREADY_EXIST,
                response_message=response_codes.MESSAGE_ALREADY_EXISTS_DATA,
                response_data=already_exists
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
                    constants.CLIENT.title(), constants.ID
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
                constants.GAMEUNIT.title(), constants.ID
            ))
        
    @classmethod
    def get_rfcards(cls,data):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[obj.display_min() for obj in cls.db_read_records(read_filter=data)],
        )
        
    @classmethod
    def get_rfcards_org(cls,data):
        
        obj = cls.db_read_records(read_filter={constants.RFCARD__ORGANIZATION:data[constants.RFCARD__ORGANIZATION]})
        card_id_list = [rfcard.display_card_id() for rfcard in obj]
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=card_id_list
        )
        
    @classmethod
    def get_rfcards_branch(cls,data):
        
        obj = cls.db_read_records(read_filter={constants.RFCARD__BRANCH:data[constants.RFCARD__BRANCH]})
        card_id_list = [rfcard.display_card_id() for rfcard in obj]
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=card_id_list
        )
    
    @classmethod 
    def get_card_id_list(cls, data):

        obj = cls.db_read_records(read_filter={constants.RFCARD__UID:data[constants.RFCARD__UID]})
        card_id_list = [rfcard.display_card_id() for rfcard in obj]
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data= card_id_list)
        
    @classmethod
    def get_rfcard_ids(cls):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[{'id':str(obj[constants.ID]), 'card_id':obj[constants.RFCARD__ID],'card_uid':obj[constants.RFCARD__UID] } for obj in cls.db_read_records(read_filter={})],
        )
    
