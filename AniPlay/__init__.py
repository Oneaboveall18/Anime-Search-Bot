import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "9452628")),
    api_hash= os.environ.get("API_HASH", "8a5a99bcf763a60913f9d74d79e501cb
"),
    bot_token= os.environ.get("TOKEN", "5904416067:AAHSLcgt4v6J_uvtzMVkqC7fRryn3xxHkI8
")
)
