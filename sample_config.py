import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("1184443346:AAH7vfrBDVOmyfkcaHn2_z5wVQUi0BFGgxI", None)
    # required for running on Heroku
    URL = os.environ.get("https://freedomuz.heroku.com", "")
    PORT = int(os.environ.get("PORT", 5000))
    # get a token from ChatBase.com for analytics
    CBTOKEN = os.environ.get('69e35e5d-bab9-4e27-afa0-6d7f7e80269f', None)
    # Python3 ReQuests CHUNK SIZE
    CHUNK_SIZE = 10281
    # ReMove.BG API Key
    REM_BG_API_KEY = os.environ.get("zqXidnMMFeVdd21AexuMfAAe ", None)
    # temporary download location
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")
