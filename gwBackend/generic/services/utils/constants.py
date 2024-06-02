# Python imports
import json

# Local imports
from gwBackend import config


# Reading Static Data
static_data = {}
with open(config.static_data_path, "r") as static_data_file:
    static_data = json.load(static_data_file)

# Validation Response Messages
VALIDATION_MESSAGES = {
    "REQUIRED": "{} is required",
    "NONEXISTENT": "{} should not be provided",
    "UNIQUE": "{} has to be unique",
    "EXISTS": "{} with this {} does not exist",
    "PASSWORD": {
        "MINIMUM_LENGTH_ERROR": "{} must contain minimum 8 characters",
        "MISSING_LOWERCASE": "{} must contain a single LowerCase character",
        "MISSING_UPPERCASE": "{} must contain a single UpperCase character",
        "MISSING_NUMBER": "{} must contain a single Number",
        "MISSING_SPECIAL": "{} must contain a single Special character",
    },
    "UID": "Please Enter a Valid {}",
    "EMAIL": "Please Enter a Valid {}",
    "PHONE_NUMBER": "Please Enter a Valid {}",
    "DATATYPE": "The Field {} has to be a type of {}",
    "DATETIME_FORMAT": "The Field {} should be in valid Date Time Format i.e "
    + config.DATETIME_FORMAT,
    "DATE_FORMAT": "The Field {} has to contain a valid Date Format i.e "
    + config.DATE_FORMAT,
    "CHOICES": "The Field {} has to be a value in {}",
    "LENGTH": "The Field {} has to be of length {}",
    "MAX_LENGTH": "The Length of Field {} has to be less than {}",
    "MIN_LENGTH": "The Length of Field {} has to be greater than {}",
    "FORMAT": "The Format of Field {} is incorrect Errors : {}",
}

# Validation constants
GENDER_LIST = static_data["gender"]
# Default Validation of Data before it is inserted into the database
DEFAULT_VALIDATION = True
# Default if to read is_deleted = True records from database
DEFAULT_READ_DELETED_RECORDS = False
# Update modes Database Layer
UPDATE_MODE__FULL = "full"
UPDATE_MODE__PARTIAL = "partial"

# DEFAULT OBJECTS
OBJECT_STATUS_ACTIVE = static_data["statuses"][0]
OBJECT_STATUS_INACTIVE = static_data["statuses"][1]
OBJECT_STATUS_SUSPENDED = static_data["statuses"][2]
# DEFAULT ROLES
DEFAULT_ADMIN_ROLE_OBJECT = static_data["user_roles_and_rights"][0]
DEFAULT_OWNER_ROLE_OBJECT = static_data["user_roles_and_rights"][1]
DEFAULT_MG_ROLE_OBJECT = static_data["user_roles_and_rights"][2]
DEFAULT_FI_ROLE_OBJECT = static_data["user_roles_and_rights"][3]
DEFAULT_ROLE_OBJECTS = [
    DEFAULT_ADMIN_ROLE_OBJECT,
    DEFAULT_OWNER_ROLE_OBJECT,
    DEFAULT_MG_ROLE_OBJECT,
    DEFAULT_FI_ROLE_OBJECT,
]

OBJECT_STATUS_ACTIVE_ID = 1
OBJECT_STATUS_INACTIVE_ID = 2
OBJECT_STATUS_SUSPENDED_ID = 3


# STARTING
STATIC_DATA = static_data

SEARCH_DEPTH_MAX = 3

# USER TYPES
ADMIN = "admin"
OWNER = "owner"
MG = "mg"
FI = "fi"

# USER ROLE IDS
ROLE_ID_ADMIN = 1
ROLE_ID_OWNER = 2
ROLE_ID_MG = 3
ROLE_ID_FI = 4

# ENDING


ID = "id"
STATUS = "status"
STATUS__ID = "id"
STATUS__NAME = "name"
CREATED_ON = "created_on"
UPDATED_ON = "updated_on"
CREATED_BY = "created_by"
UPDATED_BY = "updated_by"


CURRENT_TIME = "current_time"

ADDRESS__COUNTRY = "country"
ADDRESS__PROVINCE = "province"
ADDRESS__CITY = "city"
ADDRESS__AREA = "area"
ADDRESS__STREET_ADDRESS = "street_address"

ADDRESS_VALIDATION_FORMAT = {
    "key": [
        {
            "rule": "choices",
            "options": [
                ADDRESS__COUNTRY,
                ADDRESS__PROVINCE,
                ADDRESS__CITY,
                ADDRESS__AREA,
                ADDRESS__STREET_ADDRESS,
            ],
        }
    ],
    "value": [{"rule": "required"}, {"rule": "datatype", "datatype": str}],
}

FILTER__NEW = "new"
FILTER__OLD = "old"
FILTER_LIST = [FILTER__NEW, FILTER__OLD]

# USER LOGIN CHANNELS
EMAIL = "email"
PHONE = "phone"
LOGGED_IN_USER = "logged_in_user"
PLATFORM_WEB = 'web'
PLATFORM_MOBILE = 'mobile'
PLATFORM_DEVICE = 'iot'
PURPOSE_LOGIN = "login-user"
PURPOSE_RESET_PASSWORD = "reset-password"

# Change Password Email
# PLATFORM_EMAIL = 'email'


# USER CONSTANTS
USER = "user"
USER__NAME = "name"
USER__EMAIL_ADDRESS = "email_address"
USER__CITY = "city"
USER__CARD_ID = "card_id"
USER__PHONE_NUMBER = "phone_number"
USER__PASSWORD = "password"
USER__GENDER = "gender"
USER__NIC = "nic"
USER__ROLE = "role"
USER__MANAGER = "manager"
USER__ROLE__ROLE_ID = "user_role_id"
USER__ROLE__NAME = "name"
USER__ROLE__TITLE = "title"
USER__ROLE__RIGHTS = "rights"
USER__ROLE__MANAGER = "manager"
USER__ROLE__MANAGER_ID = "manager_id"
USER__ROLE__MANAGER_NAME = "manager_name"
USER__BRANCH = "branch"

USER__NEW_PASSWORD = "new_password"
USER__OLD_PASSWORD = "old_password"

# Required, Optional Fields Lists
# User
LOGIN_REQUIRED_FIELDS_LIST = [USER__EMAIL_ADDRESS, USER__PASSWORD]
REQUIRED_FIELDS_LIST__USER = [
    USER__NAME,
    USER__EMAIL_ADDRESS,
    USER__PASSWORD,
    USER__PHONE_NUMBER,
    USER__CITY,
    USER__CARD_ID,
    USER__GENDER,
    USER__ROLE,
    USER__NIC
]
OPTIONAL_FIELDS_LIST__USER = [
    USER__EMAIL_ADDRESS,
    USER__PHONE_NUMBER,
    # USER__ROLE__MANAGER_NAME,
    USER__MANAGER]
REQUIRED_UPDATE_FIELDS_LIST__USER = list(
    set(REQUIRED_FIELDS_LIST__USER + [ID])
    - set([USER__PASSWORD, USER__EMAIL_ADDRESS, USER__PHONE_NUMBER])
)
ALL_FIELDS_LIST__USER = OPTIONAL_FIELDS_LIST__USER + \
    REQUIRED_FIELDS_LIST__USER + [ID]


# TOKEN Constants
TOKEN = "token"
TOKEN__ACCESS_TOKEN = "access_token"
TOKEN__USER = "user"
TOKEN__PURPOSE = "purpose"
TOKEN__EXPIRY_TIME = "expiry_time"
TOKEN__IS_EXPIRED = "is_expired"
TOKEN__IS_REVOKED = "is_revoked"
TOKEN__PLATFORM = "platform"

# GAMEUNIT CONSTANTS:>>>>>>
GAMEUNIT = "game_unit"
GAMEUNIT__NAME = "name"
GAMEUNIT__ID = "gu_id"
GAMEUNIT__TYPE = "type"
GAMEUNIT__BRANCH = "branch"
GAMEUNIT__GAME_LEVEL = "game_level"
GAMEUNIT__PLAY_COUNT = "play_count"
GAMEUNIT__UNIT_STATUS = "unit_status"
GAMEUNIT__GAME_STATUS = "game_status"
GAMEUNIT__COST = "cost"
GAMEUNIT__ACCESS_TOKEN = "access_token"

# REQUIRED_FIELDS_LIST__GAMEUNIT:
REQUIRED_FIELDS_LIST__GAMEUNIT = [
GAMEUNIT__NAME,
GAMEUNIT__TYPE,
GAMEUNIT__GAME_LEVEL,
GAMEUNIT__UNIT_STATUS,
GAMEUNIT__COST
]

REQUIRED_UPDATE_FIELDS_LIST__GAMEUNIT = list(
    set([ID])
)
ALL_FIELDS_LIST__GAMEUNIT =REQUIRED_FIELDS_LIST__GAMEUNIT+ [ID, CREATED_BY, CREATED_ON]

# RESERVATION CONSTANTS>>>>>>>>>
RESERVATION = "reservation"
RESERVATION__GAME_ID = "game_id"
RESERVATION__CUSTOMER_ID = "customer_id"
RESERVATION__TIME_SLOT = "time_slot"
RESERVATION__RESV_STATUS = "resv_status"

# REQUIRED FIELD LIST RESERVATION>>>>>>>>>
REQUIRED_FIELDS_LIST__RESERVATION = [
RESERVATION__GAME_ID,
RESERVATION__CUSTOMER_ID,
RESERVATION__TIME_SLOT,
RESERVATION__RESV_STATUS,   
]
REQUIRED_UPDATE_FIELDS_LIST__RESERVATION = list(
    set([ID])
)
ALL_FIELDS_LIST__RESERVATION =REQUIRED_FIELDS_LIST__RESERVATION+ [ID, CREATED_BY, CREATED_ON]


# Member Constants
MEMBER = "member"
MEMBER__ID = "member_id"
MEMBER__NAME = "name"
MEMBER__NIC = "nic"
MEMBER__PHONE_NUMBER = "phone_number"
MEMBER__EMAIL_ADDRESS = "email_address"
MEMBER__PROFILES = "profiles"
MEMBER__MEMBERSHIP_LEVEL = "membership_level"
MEMBER__CITY = "city"
MEMBER__CARD_UID = "card_uid"

#REQUIRED Clients FIELD LIST
REQUIRED_FIELDS_LIST__MEMBERS = [
    MEMBER__NAME,
    MEMBER__PHONE_NUMBER,
    MEMBER__EMAIL_ADDRESS,
    MEMBER__MEMBERSHIP_LEVEL,
    MEMBER__CITY,
    MEMBER__CARD_UID
]

ALL_FIELDS_LIST__MEMBERS =REQUIRED_FIELDS_LIST__MEMBERS + [ID, CREATED_BY, CREATED_ON]

# profile constants

PROFILE = "profile"
PROFILE__NAME = "name"
PROFILE__CARD_ID = "card_id"
PROFILE__CREDIT = "credit"
PROFILE__REWARD = "reward"
PROFILE__GAME_HISTORY = "game_history"
PROFILE__MEMBER_ID = "member_id"


REQUIRED_FIELDS_LIST__PROFILE = [
    PROFILE__NAME,
    PROFILE__CARD_ID,
    PROFILE__CREDIT,
    PROFILE__MEMBER_ID
]

# Branch Constants
BRANCH = "branch"
BRANCH__ID = "branch_id"
BRANCH__NAME = "name"
BRANCH__LOCATION_LNG = "location_lng"
BRANCH__LOCATION_LAT = "location_lat"
BRANCH__CITY = "city"
BRANCH__GAME_TYPES = "game_types"
BRANCH__USERS = "users"
BRANCH__OPENING_TIME = "opening_time"
BRANCH__CLOSING_TIME = "closing_time"

# REQUIRED BRANCH FIELD LIST
REQUIRED_FIELDS_LIST__BRANCH = [
    BRANCH__NAME,
    BRANCH__CITY,
    BRANCH__GAME_TYPES,
    BRANCH__OPENING_TIME,
    BRANCH__CLOSING_TIME,
]

#OPTIONAL BRANCH FIELD LIST
OPTIONAL_FIELDS_LIST__BRANCH = [
    BRANCH__LOCATION_LNG,
    BRANCH__LOCATION_LAT,
    BRANCH__USERS,
]
REQUIRED_UPDATE_FIELDS_LIST__BRANCH = list(
    set([ID])
)
ALL_FIELDS_LIST__BRANCH = OPTIONAL_FIELDS_LIST__BRANCH + \
    REQUIRED_FIELDS_LIST__BRANCH + [ID, CREATED_BY, CREATED_ON]


# Rf card constants
RFCARD = "rfcard"
RFCARD__UID = "card_uid"
RFCARD__BRANCH = "branch"
RFCARD__ASSIGNED = "assigned"

REQUIRED_FIELDS_LIST__RFCARD = [
    RFCARD__UID,
    RFCARD__BRANCH,
]