import os
import random as rand
import tkinter as tk

import geopy.distance
from colorama import Fore, Style

from countries_database import countries, countries_latlongs, country_img


def guess_key(c: str) -> int:
    for key, value in countries.items():
        if value == c:
            return int(key)
    return -1


def game():
    country_key = rand.randint(1, len(countries))
    country = countries[f"{country_key}"]

    distance = var_distance.get()

    user_dif = var_difficulty.get()
    if user_dif == "Easy":
        guess = 10
    elif user_dif == "Normal":
        guess = 5
    elif user_dif == "Hard":
        guess = 3

    result = tk.Label(window, text="")

    country_ascii_key = country
    country_file = country_img[country_ascii_key]
    f = open(f'country_ascii/{country_file}.txt', 'r')
    ascii_art = f.read()

    def check_guess():
        nonlocal guess
        nonlocal country
        nonlocal result
        country_guess = entry_guess.get()
        if country_guess == country:
            result.config(text="You got it", fg="green")
            result.pack()
        else:
            guess_country_key = guess_key(country_guess)
            if guess_country_key == -1:
                result.config(text="Not in our database")
                result.pack()
            else:
                created_country = countries[country_key]
                guess_country = countries[guess_country_key]
                country, lat, long = countries_latlongs[country_key]
                created_country_latlong = (f"{lat}, {long}")
                country, lat, long = countries_latlongs[guess_country_key]
                guess_country_latlong = (f"{lat}, {long}")
                if "mi" in distance:
                    result.config(text=f"Not quite, you are {round((geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).mi)} mi away", fg="red")
                    result.pack()
                elif "km" or "kilo" in distance:
                    result.config(text=f"Not quite, you are {round((geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).km)} km away", fg="red")
                    result.pack()
        guess -= 1
        if guess == 0:
            result.config(text=f"Sorry, the country was {country}", fg="red")
            result.pack()

    label = tk.Label(window, text="Enter your guess (use '_' instead of spaces)")
    label.pack()

    entry_guess = tk.Entry(window)
    entry_guess.pack()

    button_submit = tk.Button(window, text="Submit", command=check_guess)
    button_submit.pack()

    label_art = tk.Label(window, text=ascii_art)
    label_art.pack()

    return


# main code block
# start the game by displaying a welcome text
start = open('welcome_banner.txt', 'r')
print(start.read())

# create a window
window = tk.Tk()
window.title("Country Guesser")

# create a label and pack it into the window
label = tk.Label(window, text="Press start to play")
label.pack()

# create radio buttons for distance selection
var_distance = tk.StringVar()
radio_mi = tk.Radiobutton(window, text="Miles", variable=var_distance, value="mi")
radio_km = tk.Radiobutton(window, text="Kilometers", variable=var_distance, value="km")
radio_mi.pack()
radio_km.pack()