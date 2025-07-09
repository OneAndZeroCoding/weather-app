#CUSTOMTKINTER CODE GOES HERE
import customtkinter as ctk
import config
import api
import logging
logging.basicConfig(level=logging.INFO)
logging.info("UI loaded.")

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #------window configuaration
        self.title("Weather App")
        self.geometry(config.WINDOW_SIZE)
        ctk.set_appearance_mode(config.DEFAULT_THEME_MODE)
        ctk.set_default_color_theme(config.DEFAULT_THEME)

        #-----Layout

        #-----City input
        self.city_input = ctk.CTkEntry(self, placeholder_text=f"City: {config.DEFAULT_CITY}")
        self.city_input.pack(pady=20)

        #-----Get weather
        self.get_weather_button = ctk.CTkButton(self, text="Get weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        #-----result layout
        self.result_label = ctk.CTkLabel(self, text="Result will be here")
        self.result_label.pack(pady=30)

    def get_weather(self):
        city = self.city_input.get().strip()

        if not city:
            city = config.DEFAULT_CITY
        
        try:
            weather = api.get_weather_data(city)
            logging.info("Data recieved")

            if "error" in weather:
                self.result_label.configure(text=f"{weather['error']}")

            display = (
                f"City : {weather['city']}\n"
                f"Temperature: {weather['temperature']}°C\n"
                f"Condition: {weather['desc'].title()}"
            )
            self.result_label.configure(text=display)
        except Exception as e:
            logging.error(f"Error : {e}")
