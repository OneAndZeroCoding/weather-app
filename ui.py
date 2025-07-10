#CUSTOMTKINTER CODE GOES HERE
import customtkinter as ctk
from PIL import Image
import tkinter as tk
import config
from config import ACTIVE_THEME
import api
import utils
from logger import get_logger

logger = get_logger(__name__)
logger.debug("UI module loaded")

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #------window configuaration
        self.title("Weather App")
        self.geometry(config.WINDOW_SIZE)
        self.resizable(False, False)
        self.configure(fg_color=ACTIVE_THEME['background'])
        ctk.set_appearance_mode(config.DEFAULT_THEME_MODE)
        ctk.set_default_color_theme(config.DEFAULT_THEME)

        #App variable
        self.city = ctk.StringVar()

        #-----Layout
        
        #-----Heaing
        self.heading = ctk.CTkLabel(self, text="Weather Fetcher", text_color=ACTIVE_THEME['info_panel'], font=(config.DEFAULT_FONT, 20))
        self.heading.pack(pady=10)

        #-----Weather reponse
        self.response_frame = ctk.CTkFrame(self, fg_color=ACTIVE_THEME['info_panel'])
        self.response_frame.pack(expand=True, fill="both", padx=20)

        #-----always on widgets on frame
        self.time_label = ctk.CTkLabel(self.response_frame, font=(config.DEFAULT_FONT, 15))
        self.after(1000, self.time_label.configure(text=utils.show_time()))
        self.time_label.pack(pady=10)

        #-----City input
        self.city_input = ctk.CTkEntry(self, height=50, fg_color=ACTIVE_THEME['input'], justify="center", corner_radius=20,border_width=2, textvariable=self.city, placeholder_text=f"City: {config.DEFAULT_CITY}")
        self.city_input.pack(pady=(20,0), padx=20, fill="x")

        #-----Get weather Button
        self.search_image = ctk.CTkImage(light_image=Image.open("./assets/search.png"))
        self.get_weather_button = ctk.CTkButton(self, height=50, fg_color=ACTIVE_THEME['button'], image=self.search_image, compound="left", text="Get Weather", font=(config.DEFAULT_FONT, 15), command=lambda: self.load_response_widgets(self.response_frame))
        self.get_weather_button.pack(pady=(10), padx=20, fill='x')

        logger.info("UI loaded successfully")

    # def get_weather(self):
    #     city = self.city_input.get().strip()

    #     if not city:
    #         city = config.DEFAULT_CITY
        
    #     try:
    #         weather = api.get_weather_data(city)
    #         logger.info("Response Data recieved")

    #         if "error" in weather:
    #             self.result_label.configure(text=f"{weather['error']}")
    #             logger.error(f"Error message : {weather.get("error")}")

    #         display = (
    #             f"City : {weather['city']}\n"
    #             f"Temperature: {weather['temperature']}°C\n"
    #             f"Condition: {weather['desc'].title()}"
    #         )
    #         self.result_label.configure(text="Result will be here.")
    #         logger.info("Info displayed.")

    #     except Exception as e:
    #         logger.error(f"Error : {e}")

    def load_response_widgets(self, parent):

        #frame Creations
        temp_frame = ctk.CTkFrame(parent)

        #creating labels
        error_label = ctk.CTkLabel(parent)
        city_label = ctk.CTkLabel(parent)
        temp_label = ctk.CTkLabel(temp_frame)
        icon_label = ctk.CTkLabel(temp_frame)
        error_label = ctk.CTkLabel(parent)

        #getting weather info
        weather_response = api.get_weather_data(self.city.get())
        logger.info("Response data recieved")

        if "error" in weather_response:
            error_label.configure(font=(config.DEFAULT_FONT, 15), text=f"{weather_response.get("error")}")
            error_label.pack(anchor="center", expand=True)
            logger.error(f"Error : {weather_response.get("error")}")
        else:
            error_label.destroy()
            city_label.configure(text=weather_response['city'], font=(config.DEFAULT_FONT, 20))
            temp_label.configure(text=f"{weather_response['temperature']}")
            icon = ctk.CTkImage(light_image=Image.open("./assets/settings-dark.png"))
            icon_label.configure(text="", image=icon)
            city_label.pack()
            icon_label.pack(side='left')
            temp_label.pack(side='left')
            temp_frame.pack()
