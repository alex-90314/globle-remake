#imported modules
import os
import random as rand

import geopy.distance
from colorama import Fore, Style

from countries_database import countries, countries_latlongs, country_img


#function definitions
def guess_key(c:str)->int:
  for key, value in countries.items():
    if value == c:
      return int(key)
  return -1

#main code block
#start the game by displaying a welcome text & clearing the screen
try:
	os.system("cls")
	os.system("clear")
except:
	None

start = open('welcome_banner.txt','r')
print(start.read())
cont = input("\nPress enter to start the game\n")

#generate the random country that will be used later in the code
country_key = rand.randint(1,len(countries))
country = (countries[f"{country_key}"])

#have the user select their unit
distance = input("Would you like the distance in miles or kilometers?\n")
while distance not in ("mi", "km", "kilo", "miles", "mile", "kilometers"):
  distance = input("Would you like the distance in miles or kilometers?\n")

#have the user be able to choose their difficulty
print("\ndifficulties: easy (10 guesses)/normal (5 guesses)/hard (3 guesses)")
user_dif = input("Enter desired difficulty: ")
while user_dif not in ("easy", "Easy", "normal", "Normal", "hard", "Hard"):
  user_dif = input("Enter desired difficulty: ")
  
if user_dif in ("easy", "Easy", "normal", "Normal", "hard", "Hard"):
  if user_dif == "easy" or user_dif == "Easy":
    guess = 10
  elif user_dif == "normal" or user_dif == "Normal":
    guess = 5
  elif user_dif == "hard" or user_dif == "Hard":
    guess = 3

#print the chosen country ascii & clear the screen
os.system("cls")
country_ascii_key = (country)
country_file = country_img[country_ascii_key]
f = open(f'country_ascii/{country_file}.txt','r')
print(f.read())

#prompt the user for their guess
if cont == "dev":
  print(country)
print(f"input the country name using caps and '_' instead of spaces\nex. United_States")
for i in range(guess):
  country_guess = input("Guess country: ")
  if country_guess == country:
    print(Fore.GREEN + "You got it")
    print(Style.RESET_ALL)
    break
  else:
    #use the key generated before to obtain that countries latitude and longitude
    guess_country_key = guess_key(country_guess)
    if guess_country_key == -1:
      print("Not in our database\n")
    else:
      country, lat, long = (countries_latlongs.get(country_key))
      created_country_latlong = (f"{lat}, {long}")
      country, lat, long = (countries_latlongs.get(guess_country_key))
      guess_country_latlong = (f"{lat}, {long}")
      if "mi" in distance:
        print(f"{Fore.RED}Not quite, you are {round((geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).mi)} mi away")
        print(Style.RESET_ALL)
      elif "km" or "kilo" in distance:
        print(f"{Fore.RED}Not quite, you are {round((geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).km)} km away")
        print(Style.RESET_ALL)
