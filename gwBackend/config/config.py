# Python imports
import os
# Local imports


# ENVIRONMENT = "LOCAL"
ENVIRONMENT = "STAGING"

FUNCTION_LOGGING = False

current_dir_path = os.path.dirname(os.path.abspath(__file__))
static_data_path = os.path.join(current_dir_path, "static//static_data.json")
upload_files_path = os.path.join(os.getcwd(), "//uploads")


#  EXPIRY TIME IN HOURS
TOKEN_EXPIRY_TIME_WEB = 2
TOKEN_EXPIRY_TIME_DEVICE = 700 #days
TOKEN_EXPIRY_TIME_MOBILE = 30
TOKEN_EXPIRY_TIME_EMAIL = 0.5

FIREBASE_CONFIG = {}

FCM_API_KEY = ""


# Order VAT Rate i.e 1.15 = 15%
VAT_RATE = 1.15
# Newly Launched Filter Data Days
FILTER__NEW__TIME_DAYS = -30

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DISPLAY_DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"
DISPLAY_DATE_FORMAT = "%d-%m-%Y"
DISPLAY_TIME_FORMAT = "%H:%M:%S"
FILTER_DATE_FORMAT = "%d %m %Y"
FILTER_DATETIME_FORMAT = "%d %m %Y %H:%M:%S"
TIME_ZONE = "Asia/Karachi"

FRONTEND_URL = "https://api.thedragonzone.com"
MONGO_DB_USER = "munas"
MONGO_DB_PASSWORD = "k9QauSm0wACivnIO"
DATABASE_NAME = "dragonzone"

MONGO_DB_URI = ""
if ENVIRONMENT == "LOCAL":
    MONGO_DB_URI = f"mongodb://localhost:27017/{DATABASE_NAME}"
if ENVIRONMENT == "STAGING":
    FUNCTION_LOGGING = True
    static_data_path = os.path.join(
        current_dir_path, "static/static_data.json")
    upload_files_path = os.path.join(current_dir_path, "static/uploads")
    # MONGO_DB_URI = f"mongodb://192.168.100.8:27017/gwBackend"
    MONGO_DB_URI = f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@munas-california.inrzszt.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority"


DEFAULT_ADMIN_NAME = "Admin"
DEFAULT_ADMIN_EMAIL = "admin@mail.com"
DEFAULT_ADMIN_PASSWORD = "Alchohol@123"
DEFAULT_ADMIN_PHONE = "+9233121212"
DEFAULT_ADMIN_CITY = "Karachi"
DEFAULT_ADMIN_CARD_ID = "C3CD1204"
DEFAULT_BRANCH_NAME = "Headoffice"
DEFAULT_BRANCH_CITY = "Karachi"
DEFAULT_BRANCH_OPENING_TIME = "0900"
DEFAULT_BRANCH_CLOSING_TIME = "1700"
DEFAULT_BRANCH_GAME_TYPES = []
DEFAULT_BRANCH_PERCENTAGE = 100
DEFAULT_BRANCH_CREDIT_LIMIT = 100000
DEFAULT_ADMIN_ORGANIZATION_NAME = "DRAGON ZONE"
DEFAULT_ADMIN_ORGANIZATION_PERCENTAGE = 100
DEFAULT_ADMIN_ADDRESS = "Karachi"
DEFAULT_ADMIN_COUNTRY = "Pakistan"
DEFAULT_WEB = "http://portal.thedragonzone.com/updatemember/"


DUMMY_NAME = ""
DUMMY_EMAIL = ""
DUMMY_PASSWORD = ""
DUMMY_PHONE = ""
DUMMY_CITY = ""
# DUMMY_CARD_ID = "C3CD1204"
DUMMY_ADDRESS = ""
DUMMY_COUNTRY = ""
DUMMY_GENDER = ""


DUMMY_MEMBER_NAME = ""
DUMMY_MEMBER_MEMBERSHIP_LEVEL = "Basic"
DUMMY_MEMBER_REWARD = ""
DUMMY_MEMBER_GAME_HISTORY = {}
DUMMY_MEMBER_CREDIT = 0
DUMMY_MEMBER_TYPE = ""
DUMMY_MEMBER_CITY = ""


# EMAIL_USER = "gwBackend316@gmail.com"
# EMAIL_PASSWORD = "gwBackend123"

MAIL_SETTINGS = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "admin@mail.com",
    "MAIL_PASSWORD": "Admin@123"
}
