import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

load_dotenv()
que = {}
admins = {}
SESSION_NAME = 1AZWarzUBu8E7RAVIkeTiG_igMnAahxDVVFzeDjCV8p7VH8a-_G08RfQ1-7H9toqRG7e8F3bX_cZ3HdD9ZyYCxMajfO-sGdUsvz3nPTceMjV4g7uYlmqh35LGf_OlZxEYjPYpyGImjsi_vQa-NHGjqR_mN0uBkGq_epG5lrDWUcnbkjozuGXqCywDAcjpZ3HpmVizTE8gtg09BNd8vX77_plWq6AeHp4UGFQJ7oDnhh38h09Zl3DffT5GGI3TC4gmtSXVbKvcifcgF1ztubl7Xo7m_WeFvFQlx7idSbiO3NJ-dKEDijAfzbFsRIbz0cNCwsQsC8WCVO6V0Ae9rXeyuPwpdHMMr_s=
BOT_TOKEN = 1628785224:AAFqfvW9Uia5nux-3G0S149fVMw6wA2ML3Q
BOT_NAME = Emcee 
BG_IMAGE = https://telegra.ph/file/f2e20442268dfeff8d405.png
THUMB_IMG = https://telegra.ph/file/f2e20442268dfeff8d405.png
AUD_IMG = https://telegra.ph/file/f2e20442268dfeff8d405.png
QUE_IMG = https://telegra.ph/file/f2e20442268dfeff8d405.png
API_ID = 8412601
API_HASH = 16e3ee37b54aa708e8250e270a531d89
BOT_USERNAME = Emcee_bot
ASSISTANT_NAME = EmceeVcPlayer
GROUP_SUPPORT = Emcee_Support
UPDATES_CHANNEL = Emcee_Updates
OWNER_NAME = Yato
PMPERMIT = NONE
OWNER_ID = 
DATABASE_URL = MONGO_DB_URI2 = mongodb+srv://abc:abc@cluster0.ye0s8.mongodb.net/test?retryWrites=true&w=majority
LOG_CHANNEL = -1001581899215
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = 1717636238
LANG = EN
