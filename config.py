#CONSTANTS AND CONFIG SETTINGS
import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)
logging.info("CONSTANTS loaded.")

#loading env
load_dotenv()

#-----API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")
UNITS = "metric"

#-----Custom Tkinter settings
WINDOW_SIZE = "500x300"
DEFAULT_THEME = "green"
DEFAULT_THEME_MODE = "Dark"
DEFAULT_CITY = "Hyderabad"


#-----Logging
LOG_FILE = "app.log"