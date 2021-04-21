import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or '53ca58f0a19696a3dc36e52936d2413c698f6cca0ffc383444806ba8a17f05e331572'

    MIGRATIONS_DIR = "migrations_local"

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, "static")
    USER_DIR_NAME = "user_data"
    USER_DIR = os.path.join(BASE_DIR, USER_DIR_NAME)

    USER_EMAIL_SENDER_EMAIL = "danielqmuniproject@gmail.com"
    USER_APP_NAME = "PSS"
    USER_COPYRIGHT_YEAR = 2021
    USER_CORPORATION_NAME = "ProjectDan"
    USER_UNAUTHENTICATED_ENDPOINT = 'app.index'

    AUDIO_MIME_TYPE = "audio/webm;codecs=opus"
    AUDIO_FILE_EXT = "webm"
