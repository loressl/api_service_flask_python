import pathlib
import os
from dotenv import load_dotenv

path_dir= pathlib.Path().absolute()
load_dotenv(os.path.join(path_dir, '.env'))
screteKey= os.getenv('SECRET_KEY')
database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')

ENV = ""
DEBUG = True

SQLALCHEMY_DATABASE_URI = database_uri
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY= screteKey