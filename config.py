#CONSTANTS AND CONFIG SETTINGS
import os
from dotenv import load_dotenv
from logger import get_logger

logger = get_logger(__name__)
logger.debug("Constants loaded.")

#loading env
load_dotenv()
logger.debug(".env loaded.")

#-----API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")
UNITS = "metric"

#-----Custom Tkinter settings
WINDOW_SIZE = "400x550"
DEFAULT_THEME = "blue"
DEFAULT_THEME_MODE = "Light"
DEFAULT_CITY = "Hyderabad"

#-----THEMES
themes = {
    "night":{
        "background":"#0a090c",
        "info_panel":"#F0EDEE",
        "button":"#2C666E",
        "input":"#6dd3ce",
        "text":"#696D7D"
    }
}

ACTIVE_THEME = themes["night"]

#CTK fonts
DEFAULT_FONT = "Arial"

#-----Logging
LOG_FILE = "app.log"