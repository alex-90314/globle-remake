#imported modules
import random as rand
from countries_database import countries, country_img, countries_latlongs
import geopy.distance
import os
import keyboard

#main code block
#start the game by displaying a welcome text & clearing the screen
os.system("cls")
start = open('welcome_banner.txt','r')
print (start.read())
cont = input("\nPress enter to start the game\n")

#generate the random country that will be used later in the code
key = rand.randint(0,len(countries))
country = (countries[f"{key}"])

#have the user be able to choose their difficulty
print("difficulties: easy (10 guesses)/normal (5 guesses)/hard (3 guesses)")
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
key2 = (country)
country_file = country_img[key2]
f = open(f'country_ascii/{country_file}.txt','r')
print(f.read())

#prompt the user for their guess
print (country)
print (f"input the country name using caps and '_' instead of spaces\nex. United_States")
for i in range(guess):
  country_guess = input("Guess country: ")
  if country_guess == country:
    print ("You got it")
    break
  else:
    print (country)
    #use the key generated before to obtain the same countries latitude and longitude
'''    country, lat, long = (countries_latlongs.get(key))
    created_country_latlong = (f"{lat}, {long}")
    country, lat, long = (countries_latlongs.get(guess_key))
    guess_country_latlong = (f"{lat}, {long}")
    print (f"Not quite, you are {(geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).km} away")
    print (f"Not quite, you are {(geopy.distance.geodesic(guess_country_latlong, created_country_latlong)).mi} away")'''
  