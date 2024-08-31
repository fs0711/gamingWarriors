# Python imports

# Framework imports

# Local imports
from gwBackend import config
from gwBackend.UserManagement.models.User import User
from gwBackend.generic.controllers import Controller
from gwBackend.UserManagement.controllers.TokenController import TokenController
from gwBackend.generic.services.utils import constants, response_codes, response_utils, common_utils


class UserController(Controller):
    Model = User

    @classmethod
    def create_controller(cls, data):
        data[constants.USER__ROLE] = constants.DEFAULT_ROLE_OBJECTS[int(data[constants.USER__ROLE])]
        user_manager = cls.db_read_single_record(read_filter={constants.USER__NAME : data[constants.USER__MANAGER]})
        data[constants.USER__MANAGER] = user_manager[constants.ID]
        is_valid, error_messages, obj = cls.db_insert_record(
            data=data, db_commit=False)
        if is_valid:
            obj[constants.USER__PASSWORD] = common_utils.encrypt_password(
                password=obj[constants.USER__PASSWORD])
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
    def login_controller(cls, data, platform="web"):
        if platform != constants.PLATFORM_WEB\
            and platform != constants.PLATFORM_MOBILE\
            and platform != constants.PLATFORM_DEVICE:
            return response_utils.get_json_response_object(
                response_code=response_codes.CODE_PLATFORM_INCORRECT,
                response_message=response_codes.MESSAGE_PLATFORM_INCORRECT
                .format(
                    [constants.PLATFORM_WEB, constants.PLATFORM_MOBILE, constants.PLATFORM_DEVICE]),
            )
        is_valid, error_messages = cls.cls_validate_data(data=data,
                                                         validation_rules=cls.Model.login_validation_rules())
        if is_valid:
            user = cls.db_read_single_record(read_filter={
                constants.USER__EMAIL_ADDRESS: data[constants.USER__EMAIL_ADDRESS]
            })
            if user:
                if user.verify_password(password=data[constants.USER__PASSWORD]):
                    if platform == constants.PLATFORM_WEB:
                        expiry_time = config.TOKEN_EXPIRY_TIME_WEB
                    if platform == constants.PLATFORM_MOBILE:
                        expiry_time = config.TOKEN_EXPIRY_TIME_MOBILE                    
                    if platform == constants.PLATFORM_DEVICE:
                        expiry_time = config.TOKEN_EXPIRY_TIME_DEVICE                    
                    token_is_valid, token_error_messages, token = TokenController.generate_access_token(
                        user=user, purpose=constants.PURPOSE_LOGIN,
                        expiry_time=expiry_time, platform=platform)
                    if token_is_valid:
                        return response_utils.get_json_response_object(
                            response_code=response_codes.CODE_SUCCESS,
                            response_message=response_codes.MESSAGE_LOGIN_SUCCESS,
                            response_data=token.display())

                    else:
                        return response_utils.get_json_response_object(
                            response_code=response_codes.CODE_VALIDATION_FAILED,
                            response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                            response_data=token_error_messages
                        )
                else:
                    return response_utils.get_json_response_object(
                        response_code=response_codes.CODE_INVALID_PASSWORD,
                        response_message=response_codes.MESSAGE_INVALID_DATA.format(
                            constants.USER__PASSWORD
                        ))
            else:
                return response_utils.get_json_response_object(
                    response_code=response_codes.CODE_INVALID_EMAIL_ADDRESS,
                    response_message=response_codes.MESSAGE_NOT_FOUND_DATA.format(
                        constants.USER.title(), constants.USER__EMAIL_ADDRESS
                    ))
        else:
            return response_utils.get_json_response_object(
                response_code=response_codes.CODE_VALIDATION_FAILED,
                response_message=response_codes.MESSAGE_VALIDATION_FAILED,
                response_data=error_messages
            )

    @classmethod
    def logout_controller(cls):
        logged_in_user = common_utils.current_user()
        TokenController.suspend_user_tokens(
            read_filter={constants.TOKEN__USER: logged_in_user})
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS, response_message=response_codes.MESSAGE_LOGOUT_SUCCESS
        )

    @classmethod
    def get_user_childs(cls, user, search_depth=4, return_self=True):
        user_level__dict = {
            constants.ADMIN: 4
        }
        user_level = user_level__dict[user[constants.USER__ROLE]
                                      [constants.USER__ROLE__NAME]]
        if user_level > search_depth:
            user_level = search_depth
        if user_level == 4:
            return cls.db_read_records(read_filter={})
        user__childs_list = [cls.db_read_records(
            read_filter={constants.USER__MANAGER: user})]
        for _ in range(user_level-1):
            current_level_childs = cls.db_read_records(read_filter={
                constants.USER__MANAGER+"__in": user__childs_list[0]})
            user__childs_list.insert(0, current_level_childs)
        user__childs = []
        for list_childs in user__childs_list:
            user__childs.extend(list_childs)
        if return_self:
            user__childs.append(user)
        return user__childs

    @classmethod
    def get_user(cls, data):
        return cls.db_read_single_record(read_filter={constants.ID: data}, deleted_records=True)

    @classmethod
    def get_users_childs_list(cls, data):
        user_childs = UserController.get_user_childs(
            user=common_utils.current_user(), return_self=True)
        child_list = [user.display() for user in user_childs]
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_LOGIN_SUCCESS,
            response_data=child_list)
    
    @classmethod 
    def get_user_list(cls, data):
        obj = cls.db_read_records(read_filter={constants.USER__ROLE:{"name":data[constants.USER__ROLE__NAME]}})
        user_list = [user.display_id() for user in obj]
        return response_utils.get_response_object(
            response_code=response_codes.CODE_SUCCESS,
            response_message=response_codes.MESSAGE_SUCCESS,
            response_data= user_list)
