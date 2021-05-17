from tkinter import *

import requests
import json

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80014&distance=38&API_KEY=03741560-4E24-4640-8807-63CA6FF23E8A


root=Tk()
root.title("weather app")
root.geometry("600x50")
bac="green"

try :
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43229&distance=38&API_KEY=03741560-4E24-4640-8807-63CA6FF23E8A")
    api=json.loads(api_request.content)
    city=api[0]["ReportingArea"]
    quality=api[0]["AQI"]
    category=api[0]["Category"]['Name']
    if category=="Good":
        weather_color="#00E400"
    elif category=="Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy":
        weather_color = "green"
    elif category == "Hazardous":
        weather_color = "green"
    root.configure(bg=weather_color)


    my_label = Label(root, text=city + "\t" + "Air quality :" + str(quality) + "\t" + category, font="arial 20 bold",
                     bg=weather_color)
    my_label.pack(fill="both")
except Exception as e:
    api="error"



root.mainloop()


