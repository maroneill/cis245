#Weather Project Martin ONeill CIS 245 Intro to Programming

#imports regular expression package to use for validating zip-code input
import re, requests, json, datetime

from requests.models import Response

#API keys for google maps and openweathermap
google_key = 'AIzaSyAZzq7I07cwkA0FAw1bY1WnTAUzAghzQW0'
weather_key = '0bf26da62486aa559df04ca8365c494e'



daily = ''

#converts user city or zip to lat / lon to use with openweathermaps
def get_coordinates():
    r = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={user_location}&key={google_key}").json()   
    if r['status'] == 'OK':
        global lat, lon
        geometry = r['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

    else:
        print("No results found.")

def get_weather():
    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid={weather_key}").json()
    tday = 0
    for days in range(0,7):
        daily = r['daily'][days]['temp']['day']
        print(f"\t\tWeather for " + str(datetime.date.today() + datetime.timedelta(tday)) + " is " + str(int(daily)) + "°")
        tday += 1
    

#function for user to choose city or zipcode input
def zip_or_city():
    zip_or_city = int(input(f"\n\t1:Forecast by City name\n\t2:Forecast by Zip-Code\n\nPlease select an option:"))
    if zip_or_city == 1:
        validate_city(input)
        get_coordinates()
        get_weather()
    elif zip_or_city == 2:
        validate_zip(input)
        get_coordinates()
        get_weather()
    else:
        print(f"Please choose a valid option\n")
        

#function to receive and validate a zip code with RegEx
def validate_zip(input):
    while True:
        global user_location
        legit_zipcode = "^[0-9]{5}(?:-[0-9]{4})?$"
        user_location = input(f"\nPlease enter your 5 digit zipcode: ")
        if (re.search(legit_zipcode, user_location)):
            return user_location  
        else:
            print(f"{user_location} is not a valid zip-code.")

#function to receive and validate a city name with RegEx
def validate_city(input):
    while True:
        global user_location
        legit_city = "^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$"
        user_location = input(f"\nPlease enter your desired city: ")
        if (re.search(legit_city, user_location)):
            return user_location  
        else:
            print(f"{user_location} is not a valid city.")

#function to turn user input into API friendly input
#def formatted_input():
   # print("do something here")


#function to run main program
while True:
    print(f"Hello, thanks for using our weather program.")
    zip_or_city()
    print(f"\tGetting weather data for {user_location}...")

