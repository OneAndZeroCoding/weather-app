#LAUNCHING AND SET UP
from ui import WeatherApp
import logging
import config
import ui
import api

logging.basicConfig(level=logging.INFO)
logging.info("Main app started")

if __name__=="__main__":
    app = WeatherApp()
    app.mainloop()