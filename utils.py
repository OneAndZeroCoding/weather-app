from logger import get_logger
logger = get_logger(__name__)

import time

def show_time():
    current_time = time.strftime("%I:%M %p")
    return current_time

logger.debug("Utils loaded.")