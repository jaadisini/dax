import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "26917284"))
API_HASH = getenv("API_HASH", "e89fc9ea865e7494f742dab7132d28f9")

EVAL = list(map(int, getenv("EVAL", "7149602071").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7250836835:AAGWmAAeQn4bhTbuMW1RhGHc9nCVS6_rXUQ")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Dza4yu")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Dzamusikbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "𝗗𝘇𝗮 ✘ 𝗠𝗨𝗦𝗜𝗖")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "DzaAssistant")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://jembutan1:1234@cluster0.w186hoa.mongodb.net/?retryWrites=true&w=majority")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002149981793))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 1543559565))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/jaadisini/dax",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/zeropercentdza")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DzaSupport")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQHHpwsAtvgB-qU7FMotcXVrSpOHLLUGe62cfmnaZ2Nsa3v3pcOScuHjOF5iS2gmSbEqpvizivjcNp0YQpJ1F64WWfkahHZLNTY4rz8ZeFDunXmZGpRaw8zmIDrmN9eYlDV_RisEPM_3Pz3IaszXa3bVpdDVeHeoDrc2-d3Tua5RKehuFN06sDTqgG4ueDVlvI8wXnEcR_u73NdJ7o-Amq9xLsV6Uxlk1b38LINmaVmoWan6LGxbWi6l7gvgSshsRtzyrAp_6KoKJ9i9OEqBot_EdYgCJJ8eRkMb9ava1AMzsakwzFkrKR2USFGicASt30lwF8IUS_mvOBcjH0O30NjNZcLqCgAAAABpoUtSAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
PING_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
GLOBAL_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
STATS_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/768e52d46733806e6beee.jpg"



# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
