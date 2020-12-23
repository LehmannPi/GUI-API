# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:05:00 2020

@author: Filipe Lehmann
"""

import tkinter as tk
import requests					# pip install requests on prompt
from PIL import Image, ImageTk	# pip intall pillow

HEIGHT = 400
WIDTH = 800
BOXC = "#C9DAFF"

# Example key - Obtained at openweathermap.org - Substituted for GitHub repository
# 12642673511ae759b7dc4f1234567890
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}    

def format_weather(weather):
    try:
        name = weather['name']
        cntr = weather['sys']['country']
        desc = (weather['weather'][0]['description']).capitalize()
        temp = weather['main']['temp']
        t_min = weather['main']['temp_min']
        t_max = weather['main']['temp_max']
        hum = weather['main']['humidity']
        
        fin_str = 'City: %s / %s \nCondition: %s \nTemperature: %s ºC ( %s / %s ) ºC \nHumidity: %s%% '%(name,cntr,desc,temp,t_min,t_max,hum)
    except:
        fin_str = 'There was a problem retrieving info.'
    
    return fin_str

def get_weather(city):
    api_file = open('api-key.txt', 'r')
    weather_key = api_file.read()
    api_file.close()
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url,params=params)
    weather = response.json()
    
    lbl['text'] = format_weather(weather)

root = tk.Tk()

canv = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canv.pack()

bg_jpg_im = Image.open("gradient.png")
bg_img = ImageTk.PhotoImage(bg_jpg_im)
bckg_lable = tk.Label(root, image=bg_img)
bckg_lable.image = bg_img
bckg_lable.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg=BOXC,bd=4)
frame.place(relx = 0.5, rely = 0.1, relwidth=0.3, relheight=0.18, anchor='n')

entry = tk.Entry(frame, font=18, justify = 'center')
entry.place(anchor='n', relx=0.5, rely=0.05, relwidth=0.85, relheight=0.4)

btn = tk.Button(frame, text="Get Weather", font=18, command=lambda: get_weather(entry.get()))
btn.place(relx = 0.5, rely = 0.55, anchor='n', relwidth=0.6, relheight=0.4)

lower_frame = tk.Frame(root, bg=BOXC,bd=6)
lower_frame.place(relx=0.5, rely=0.39, relwidth=0.75, relheight=0.5, anchor='n')

lbl = tk.Label(lower_frame,font = 18, bd=4)
lbl.place(relwidth=1, relheight=1)

root.mainloop()