import os
from dotenv import load_dotenv


load_dotenv()


COUNTRY_CODE = '55'
AREA_CODE = '11'
LENGTH_MIN_VALID_PHONE = 8
LENGTH_MIN_VALID_PHONE_WITHOUT_COUNTRY_CODE = [10, 11]
LENGTH_MIN_VALID_PHONE_WITHOUT_AREA_CODE = [8, 9]

INITIAL_ID = 0

DB_CONFIG = {
    'HOST': os.environ.get('DB_HOST'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'DATABASE': os.environ.get('DATABASE'),
}

BASE_URL = os.environ.get('URL_API')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
TEMPLATE_ID = os.environ.get('TEMPLATE_ID')