import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28407968"))
    API_HASH = os.environ.get("API_HASH", "422126161e78bfd7ab9ffa28a15a23f3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6163660815:AAEpPdIQgE07vdJySxM6xuQau_jgqGGGPiA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgBjEzA6rDp9TO3dstx2z0fOWu5WyFtMO-FSQvkxHQwAL5zHQRxcHe-Fk8-8DUwfQ3oe3FUKdBzw17S4gsHPcv-vSWnmMlVKebAoAJ2IbCLzCJL4jF-378OjVvIHd9isAkmRO95B5cd_A2zbBAKkpJ7TEEOZSMHBq1_WmO-ICfnFzSb9urtbVyG7m-1fVoNo-w6MoNNzzcunjRIUS-5INKlhyBdL5DZ-ydojfADRm-ohcFAj_m5f-Qopkel0J1vkSDqsSarG8HPRdDhQ4Wc5p4mME2BFUIruJkkIbm-qVvLfxxXqawAZVDtS9hGdemHi52EMEX6I70AX4ZLwkQLYhOjKAAAAAXN7xnEA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "N3zUBoT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6232458865")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
