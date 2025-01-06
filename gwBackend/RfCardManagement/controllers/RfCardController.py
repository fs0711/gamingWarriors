# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.UserManagement.controllers.UserController import UserController
from gwBackend.MembersManagement.controllers.MemberController import MemberController
from gwBackend.RfCardManagement.models.RfCard import RfCard
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class RfCardController(Controller):
    Model = RfCard

    @classmethod
    def create_controller(cls, data):
        if data.get(constants.RFCARD__BRANCH):
            data[constants.RFCARD__ASSIGNED] = True
            branch = data[constants.RFCARD__BRANCH]
        else:
            data[constants.RFCARD__ASSIGNED] = False
            branch = None
        credit = data[constants.RFCARD__CREDIT]
        del data[constants.RFCARD__CREDIT]
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
            rfcard = obj
        
            is_valid, error_messages, obj = UserController.db_insert_record(
                data={
                    constants.USER__NAME: config.DUMMY_NAME,
                    constants.USER__PHONE_NUMBER: config.DUMMY_PHONE,
                    constants.USER__GENDER: config.DUMMY_GENDER,
                    constants.USER__NIC: "123456",
                    constants.USER__ROLE: constants.DEFAULT_MB_ROLE_OBJECT,
                    constants.USER__CITY: config.DUMMY_CITY,
                    constants.USER__URL_KEY : common_utils.generate_random_string(),
                    constants.USER__CARD_ID: str(obj[constants.ID]),
                    constants.USER__BRANCH: branch,
                    constants.USER__ORGANIZATION: str(obj['organization'].fetch().id)
                }
            )
            user_id = str(obj.id)
            
            is_valid, error_messages, obj = MemberController.db_insert_record(
                data={
                    constants.MEMBER__NAME: config.DUMMY_MEMBER_NAME,
                    constants.MEMBER__NIC: "123456",
                    constants.MEMBER__MEMBERSHIP_LEVEL : config.DUMMY_MEMBER_MEMBERSHIP_LEVEL,
                    constants.MEMBER__REWARD : config.DUMMY_MEMBER_REWARD,
                    constants.MEMBER__GAME_HISTORY : config.DUMMY_MEMBER_GAME_HISTORY,
                    constants.MEMBER__CREDIT : credit,
                    constants.MEMBER__TYPE : config.DUMMY_MEMBER_TYPE,
                    # constants.MEMBER__CITY : config.DUMMY_CITY,
                    constants.MEMBER__CARD_ID: str(rfcard[constants.ID]),
                    constants.MEMBER__ORGANIZATION_ID: str(obj['organization'].fetch().id),
                    constants.MEMBER__USER_ID :user_id
                }
            )

            return response_utils.get_response_object(
                response_code=response_codes.CODE_SUCCESS,
                response_message=response_codes.MESSAGE_SUCCESS,
                response_data=rfcard.display()
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
            obj = cls.db_read_single_record(read_filter={constants.RFCARD__ID:data})
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
        
    # @classmethod
    # def get_rfcards(cls,data):
    #     return response_utils.get_json_response_object(
    #     response_code=response_codes.CODE_SUCCESS,
    #     response_message=response_codes.MESSAGE_SUCCESS,
    #     response_data=[obj.display_min() for obj in cls.db_read_records(read_filter=data)],
    #     )
        
    # @classmethod
    # def get_rfcards_org(cls,data):
    #     obj = cls.db_read_records(read_filter={constants.RFCARD__ORGANIZATION:data[constants.RFCARD__ORGANIZATION]})
    #     card_id_list = [rfcard.display_card_id() for rfcard in obj]
    #     return response_utils.get_json_response_object(
    #     response_code=response_codes.CODE_SUCCESS,
    #     response_message=response_codes.MESSAGE_SUCCESS,
    #     response_data=card_id_list
    #     )
        
    # @classmethod
    # def get_rfcards_branch(cls,data):
    #     obj = cls.db_read_records(read_filter={constants.RFCARD__BRANCH:data[constants.RFCARD__BRANCH]})
    #     card_id_list = [rfcard.display_card_id() for rfcard in obj]
    #     return response_utils.get_json_response_object(
    #     response_code=response_codes.CODE_SUCCESS,
    #     response_message=response_codes.MESSAGE_SUCCESS,
    #     response_data=card_id_list
    #     )
    
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
        response_data=[obj.display_min() for obj in cls.db_read_records(read_filter={})],
        )
    
    @classmethod
    def transfer_rfcard(cls, data):
        # obj = cls.db_read_records(read_filter={constants.ID:data[constants.ID]})
        if data.get(constants.RFCARD__ORGANIZATION):
            update_filter={constants.RFCARD__ORGANIZATION:data[constants.RFCARD__ORGANIZATION]}
        if data.get(constants.RFCARD__BRANCH):
            update_filter={constants.RFCARD__BRANCH:data[constants.RFCARD__BRANCH],
                           constants.RFCARD__ASSIGNED: True}
        is_valid, error_message, obj = cls.db_update_records(read_filter={constants.ID+"__in":data[constants.ID]}, 
                                    update_filter=update_filter)
        if is_valid:
            if data.get(constants.RFCARD__BRANCH):
                del update_filter[constants.RFCARD__ASSIGNED]
            is_valid, error_message, obj = UserController.db_update_records(read_filter={constants.USER__CARD_ID+"__in":data[constants.ID]},
                                                                               update_filter=update_filter)
        if is_valid:
            if data.get(constants.RFCARD__ORGANIZATION):
                # if data.get(constants.RFCARD__BRANCH):
                update_filters = {constants.MEMBER__ORGANIZATION_ID: data[constants.RFCARD__ORGANIZATION]}
                    
                is_valid, error_message, obj = MemberController.db_update_records(read_filter={constants.MEMBER__CARD_ID+"__in":data[constants.ID]},
                                                                                    update_filter=update_filters)
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS
        )
