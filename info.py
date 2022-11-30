import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/396ac9984f5e94096f831.jpg https://telegra.ph/file/aff34a42a9cb577881d90.jpg https://telegra.ph/file/e94eb464fbb9a0973dd03.jpg https://telegra.ph/file/5f61ed108299807037261.jpg https://telegra.ph/file/2db80d91ea28f659c90fa.jpg https://telegra.ph/file/5cacb0cbb141eb3197f0f.jpg https://telegra.ph/file/510914d40d5692308192b.jpg https://telegra.ph/file/2e3b16e06304c6ad14e49.jpg https://telegra.ph/file/7082a76506fae563ac85a.jpg https://telegra.ph/file/78f75e23b2e728a4d06ba.jpg https://telegra.ph/file/1ab2ecfdafb58b75e6742.jpg https://telegra.ph/file/0155b2b0135258419ded1.jpg https://telegra.ph/file/6de764328690cdf1e2ab2.jpg https://telegra.ph/file/b49b23ba2e3aafa5b9592.jpg https://telegra.ph/file/c8b4ce6e1aac771630716.jpg https://telegra.ph/file/7c403d6f92c4143a4c749.jpg https://telegra.ph/file/fa3c48ac8a2c668865b4c.jpg https://telegra.ph/file/7dd2dbf32f9ca012f5c8f.jpg https://telegra.ph/file/1a4a6dcc4f75102948c10.jpg https://telegra.ph/file/6df252701c62961d98cfa.jpg https://telegra.ph/file/e4f9bcb027c81428a6e0b.jpg https://telegra.ph/file/a010a6e37f6d309b74521.jpg https://telegra.ph/file/f93667e794c3bf7f474f8.jpg https://telegra.ph/file/3fecd497e2efad783fc2a.jpg https://telegra.ph/file/722ca9f5daa20631a6889.jpg https://telegra.ph/file/722ca9f5daa20631a6889.jpg https://telegra.ph/file/df3faa3fea94cca4afd4c.jpg https://telegra.ph/file/e8ff064867944e61f6db4.jpg https://telegra.ph/file/cef6cb3314a8fce769d43.jpg https://telegra.ph/file/df8dbf1399e46a0f8965a.jpg https://telegra.ph/file/66b574ba9d723ee131b78.jpg https://telegra.ph/file/f09f2653ae29e3ad8fd78.jpg https://telegra.ph/file/ca9922fa28aee8dc4cbf7.jpg https://telegra.ph/file/7e3929cc6ccb688fbeba5.jpg https://telegra.ph/file/96cf3ed972f02349ad7c4.jpg https://telegra.ph/file/583072085ab637cd3d44b.jpg https://telegra.ph/file/3a16521edf0d77adc0c2c.jpg https://telegra.ph/file/feff30b27856c24376ebd.jpg https://telegra.ph/file/c98ba998d03841e4b59eb.jpg https://telegra.ph/file/d00cd1232e2ad13dc248d.jpg https://telegra.ph/file/6f75264775e3f50a22e88.jpg https://telegra.ph/file/328fb804a92cc2cf5a160.jpg https://telegra.ph/file/c8ee4c82b66b016b50eb8.jpg https://telegra.ph/file/4d1aa97d0d43c43667b4a.jpg https://telegra.ph/file/a181eeccd01ed83129f2e.jpg https://telegra.ph/file/1454fed6078298e3abace.jpg https://telegra.ph/file/f1fc5472a3775618b9a81.jpg https://telegra.ph/file/fb2abf2cfab842011243f.jpg https://telegra.ph/file/c75040047e7a510cf189f.jpg https://telegra.ph/file/ea1555eacf312db186d78.jpg https://telegra.ph/file/9e2697186b89845e853bb.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'heroflix_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##

      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', '')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 2000000))
SELF_DELETE = environ.get('SELF_DELETE', False)
if SELF_DELETE == "False":
    SELF_DELETE = False

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/HEROFLiX/1201"

   # Auto Delete For Bot Sending Files #
