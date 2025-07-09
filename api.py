#API FETCHING CODE
import requests
import config
import logging
logging.basicConfig(level=logging.INFO)
logging.info("API module loaded.")


def get_weather_data(city_name):
    try:
        #parameters
        params = {
            'q':city_name,
            'appid':config.API_KEY,
            'units':config.UNITS
        }
        #sending req
        logging.debug("Sending request...")
        response = requests.get(config.BASE_URL, params=params)
        logging.debug("Response recieved")

        data = response.json()
        logging.debug("Data parsed")

        code = str(data.get("cod", "200"))

        if code != "200":
            logging.info(f"API error {code}: {data.get("message")}")

            user_messages = {
                "404": "City not found. Please check again.",
                "429": "Too many requests, please slow down",
                "401": "We're having trouble connecting.",
                "502": "Server is not responding. Try again later",
                "504": "Server is busy. Try again later."
            }

            return {"error": f"{user_messages.get(code, "Unknown error. Try again in a while")}"}
            #return {"error": f"Code : {data.get("cod")}, Message : {data.get("message")}"}
        else:
            logging.debug("Status code 200")
        #main data
            weather = {
                'city': data['name'],
                "temperature": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }

            logging.info(f"Data sent")
            return weather

    except requests.ConnectionError:
        return {"error": "Please check your internet connection."}
    except Exception as e:
        logging.error(f"Error : {e}")
        return {"error": "Unexpected error occurred."}