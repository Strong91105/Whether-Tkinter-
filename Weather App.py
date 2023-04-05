# Weather App
import tkinter

import requests
from tkinter import *
from PIL import Image, ImageTk

api_key = "7ef819f1929ec112cb8ad5482882edd1"
city = None
# Frame1: Enter City
# Frame2: Weather

# Weather data from openweathermap.org

# Weather codes:
# 2xx: Thunderstorm
# 3xx: Drizzle
# 5xx: Rain
# 7xx: Atmosphere
# 8xx: Clear
# 80x: Clouds


# Setting which frame to show first
def show_frame(frame):
    frame.tkraise()



def search_city():

    city_input = enter_city.get()
    global city
    city = city_input
    global weather_data
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    print("Status code: ", weather_data.status_code)
    show_frame(frame2)

    place = city

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&APPID={api_key}")
    print("Status code: ", weather_data.status_code)

    print(weather_data.json())

    weather = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'])
    temp_min = round(weather_data.json()['main']['temp_min'])
    temp_max = round(weather_data.json()['main']['temp_max'])
    weather_state = weather_data.json()['weather'][0]['main']


    print(weather.title())
    print("Temperature: ", temp)
    print("Maximum temperature: ", temp_min)
    print("Minimum temperature: ", temp_max)
    print(weather_state.title())


    if weather_state == "Thunderstorm":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.thunder_background = thunder_background = ImageTk.PhotoImage(file="thunderbackground.jpg")
        my_canvas.create_image(0, 0, image=thunder_background, anchor="nw")
        print("Showing thunder background")

    if weather_state == "Drizzle":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.drizzle_background = drizzle_background = ImageTk.PhotoImage(file="drizzlebackground.jpg")
        my_canvas.create_image(0, 0, image=drizzle_background, anchor="nw")
        print("Showing drizzle background")

    if weather_state == "Rain":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.rain_background = rain_background = ImageTk.PhotoImage(file="rain background.jpeg")
        my_canvas.create_image(0, 0, image=rain_background, anchor="nw")
        print("Showing rainy background")

    if weather_state == "Atmosphere":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.clouds_background = clouds_background = ImageTk.PhotoImage(file="cloudybackground.jpg")
        my_canvas.create_image(0, 0, image=clouds_background, anchor="nw")
        print("Showing cloudy background")

    if weather_state == "Clear":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.clear_background = clear_background = ImageTk.PhotoImage(file="clearbackground.jpg")
        my_canvas.create_image(0, 0, image=clear_background, anchor="nw")
        print("Showing clear background")

    if weather_state == "Clouds":
        # Create a canvas
        my_canvas = Canvas(frame2, width=625, height=600)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        root.clouds_background = clouds_background = ImageTk.PhotoImage(file="cloudybackground.jpg")
        my_canvas.create_image(0,0, image=clouds_background, anchor="nw")
        print("Showing cloudy background")



    # Adding labels and buttons to canvas
    my_canvas.create_text(412, 100, text=place, font=("arial", 20))
    my_canvas.create_text(412, 170, text=str(temp) + u"\u2103", font=("arial", 40))
    my_canvas.create_text(412, 250, text=weather.title(), font=("arial", 20))
    my_canvas.create_text(412, 350, text="Min: " + str(temp_min) +u"\u2103", font=("arial", 17))
    my_canvas.create_text(412, 375, text="Max: " + str(temp_max) + u"\u2103", font=("arial", 17))

    root.logo_image = logo_image = ImageTk.PhotoImage(file="weather_transparent.png")
    button_logo = Button(frame2, image=logo_image, command=click_logo)
    button_logo_window = my_canvas.create_window(10, 10, anchor="nw", window=button_logo)




def click_logo():
    show_frame(frame1)
    print("frame1")

# Tkinter Dashboard

root = Tk()
root.title("Whether")
root.geometry('625x600')

# Frame 1 (Enter City)
frame1 = Frame(root)


background_image = ImageTk.PhotoImage(file="sunnybackground.jpg")
background_label = Label(frame1, image=background_image)
background_label.image = background_image
background_label.place(anchor=CENTER)

logo = Image.open('Weather_transparent.png')
logo = ImageTk.PhotoImage(logo)
frame1_logo_label = Label(frame1, image=logo, width=200)
frame1_logo_label.image = logo
frame1_logo_label.grid(row=0, column=0)

# Splitting cell by adding additional frame within cell
cell_split = Frame(frame1)
cell_split.grid(row=1, column=0)

enter_city = Entry(cell_split, width=10, font=("arial", 20))
enter_city.grid(row=0, column=1)

frame1_city_label = Label(cell_split, text="City:", font=("arial", 20))
frame1_city_label.grid(row=0, column=0)

# Dummy cell
dummy = Label(frame1, text="", font=("arial", 80))
dummy.grid(row=4, column=0)



search = Button(frame1, command=lambda: search_city(), text="Search?", font=("arial", 15))
search.grid(row=3, column=0, pady=20)


# Frame 2 (Weather)
frame2 = Frame(root)






for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

show_frame(frame1)


root.resizable(False, False)
root.mainloop()
