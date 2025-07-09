#LAUNCHING AND SET UP
from ui import WeatherApp
from logger import get_logger

logger = get_logger(__name__)

if __name__=="__main__":
    app = WeatherApp()
    logger.info("App initialized")
    app.mainloop()