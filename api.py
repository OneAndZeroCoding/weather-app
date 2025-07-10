#API FETCHING CODE
import requests
import config
from logger import  get_logger

logger = get_logger(__name__)
logger.debug("API module loaded")


def get_weather_data(city_name):
    try:
        #parameters
        params = {
            'q':city_name,
            'appid':config.API_KEY,
            'units':config.UNITS
        }
        #sending req
        logger.debug("Sending request...")
        response = requests.get(config.BASE_URL, params=params)
        logger.debug("Response recieved")

        data = response.json()
        logger.debug("Data parsed")

        code = str(data.get("cod", "200"))

        if code != "200":
            logger.error(f"API error {code}: {data.get("message")}")

            user_messages = {
                "404": "City not found. Please check again.",
                "429": "Too many requests, please slow down",
                "401": "We're having trouble connecting.",
                "400": "Please enter a city.",
                "502": "Server is not responding. Try again later",
                "504": "Server is busy. Try again later."
            }

            return {"error": f"{user_messages.get(code, "Unknown error. Try again in a while")}"}

        else:
            logger.debug("Status code 200")
        #main data
            weather = {
                'city': data['name'],
                "temperature": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }

            logger.info(f"Respnse data sent")
            return weather

    except requests.ConnectionError:
        logger.error(f"Error message : {e}")
        return {"error": "Please check your internet connection."}
    except Exception as e:
        logger.error(f"Unknown Error : {e}")
        return {"error": "Unexpected error occurred."}