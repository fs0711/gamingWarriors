# Python imports

# Framework imports

# Local imports
from ast import Constant
from gwBackend.generic.controllers import Controller
from gwBackend.GameunitManagement.models.Gameunit import Gameunit
from gwBackend.UserManagement.controllers.TokenController import TokenController
from gwBackend.RfCardManagement.controllers.RfCardController import RfCardController
from gwBackend.MembersManagement.controllers.MemberController import MemberController
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils, pipeline
from gwBackend import config


class GameunitController(Controller):
    Model = Gameunit

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
            constants.GAMEUNIT__TYPE+"__in": data[constants.GAMEUNIT__TYPE],
            # constants.CREATED_BY+"__nin": [current_user]
        })
        if already_exists:
            return response_utils.get_response_object(
                response_code=response_codes.CODE_USER_ALREADY_EXIST,
                response_message=response_codes.MESSAGE_ALREADY_EXISTS_DATA,
                response_data=already_exists
            )
        else:
            user = common_utils.current_user()
            #generate access token for device 
            token_is_valid, token_error_messages, token = TokenController.generate_access_token(purpose=constants.PURPOSE_LOGIN, 
                                                                                            platform=constants.PLATFORM_DEVICE, 
                                                                                            expiry_time=config.TOKEN_EXPIRY_TIME_DEVICE,
                                                                                            user=user)
            if token_is_valid:
                data.update({constants.GAMEUNIT__ACCESS_TOKEN:token[constants.TOKEN__ACCESS_TOKEN]})
                _, _, obj = cls.db_insert_record(
                    data=data, default_validation=False)
                return response_utils.get_response_object(
                    response_code=response_codes.CODE_SUCCESS,
                    response_message=response_codes.MESSAGE_SUCCESS,
                    response_data=obj.display()
                )
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
    def card_punch_controller(cls, data):
        card = RfCardController.read_UID_controller(data = data[constants.RFCARD__UID])
        if card:
            obj = cls.db_read_single_record(read_filter={
                constants.GAMEUNIT__ID:data[constants.GAMEUNIT__ID][3:]})
            recharge = MemberController.card_charge_controller(
                data={constants.MEMBER__CARD_ID:card, 
                    constants.GAMEUNIT__COST:obj[constants.GAMEUNIT__COST],
                    constants.ID:str(card[constants.ID])})
            print(recharge)
            return recharge
        else:
            return {"status":0, "name":"Unregistered"}
        
    @classmethod
    def get_gameunits(cls):
        return response_utils.get_json_response_object(
        response_code=response_codes.CODE_SUCCESS,
        response_message=response_codes.MESSAGE_SUCCESS,
        response_data=[{'game_id':obj[constants.GAMEUNIT__ID], 'name':obj[constants.GAMEUNIT__NAME],'type':obj[constants.GAMEUNIT__TYPE],'unit_status':obj[constants.GAMEUNIT__UNIT_STATUS],'cost':obj[constants.GAMEUNIT__COST],'branch':str(obj[constants.GAMEUNIT__BRANCH].fetch().name),'organization':str(obj[constants.GAMEUNIT__ORGANIZATION].fetch().name)} for obj in cls.db_read_records(read_filter={})],
        )
    
    @classmethod
    def game_cost_controller(cls, data):
        obj = cls.db_read_single_record(read_filter={
            constants.GAMEUNIT__ID:data[constants.GAMEUNIT__ID][3:]})
        return {"cost":obj[constants.GAMEUNIT__COST]}

    @classmethod
    def game_status_controller(cls):
        return {"status":1}
    
    @classmethod
    def offline_update_controller(cls, data):
        card = RfCardController.read_UID_controller(data = data[constants.RFCARD__UID])
        if card:
            obj = cls.db_read_single_record(read_filter={
                constants.GAMEUNIT__ID:data[constants.GAMEUNIT__ID][3:]})
            recharge = MemberController.bulk_card_charge_controller(
                data={constants.MEMBER__CARD_ID:card, 
                    constants.GAMEUNIT__COST:obj[constants.GAMEUNIT__COST]})
            print(recharge)
            return recharge
        else:
            return {"status":0, "name":"None"}
        
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data=data
        )