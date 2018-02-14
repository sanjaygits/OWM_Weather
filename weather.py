# Author    : Sanjay Kumar
# Purpose   : Edureka Python Self Paced Course Project.
#             Q3: Create a script called weather that return the environmental parameters
#             (temperature (min, max), windspeed, humidity, cloud, pressure, sunrise and sunset)
#             of any location you want; after passing arguments (like user api and city id).
# Date      : 14 Feb 2018
# GitHub    : https://github.com/sanjaygits/GWeather



import urllib.request
import urllib.response
import urllib.error
from pprint import pprint
import json
import time
import datetime
import sys

OWM_API = "&appid=f5d0e3664c5ab50c61cd6e3635a666ff"
OWM_URL = "http://api.openweathermap.org/data/2.5/weather?"


def query_weather_info(location, is_str):

    if is_str == True:
        query_url = OWM_URL+"q="+location.strip()+ OWM_API
    else:
        query_url = OWM_URL+"id="+str(location)+ OWM_API

    print("\nThe query url is : {}\n".format(query_url))

    #print("The query url is :"% query_url)
    #The above statement throws this: TypeError: not all arguments converted during string formatting"
    #Find out why.

    try:
        response = urllib.request.urlopen(query_url)
        resp_data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        resp_json = json.loads(resp_data.decode(encoding))       
    except urllib.error.URLError as e:
        print("\nError\n------\nException occurred!! Code: {} Reason: {}\n".format(e.code, e.reason))       
        pass
    return resp_json


def print_required_info(data):
    print("\n")
    print("------------------------------------------------")
    print("City Name             :{}".format(data['name']))
    print("City ID               :{}".format(data['id']))
    
    #The JSON temperature default is Kelvin. So adding -273.15 to the reported min and max to convert
    #to celcius
    print("Temperature - Min (C) :{}".format(-273.15+data['main']['temp_min']))
    print("Temperature - Max (C) :{}".format(-273.15+data['main']['temp_max']))

    print("Pressure(hPa)         :{}".format(data['main']['pressure']))
    print("Wind - Speed          :{}".format(data['wind']['speed']))
    print("Clouds                :{}".format(data['clouds']['all']))
    print("Clouds (Sky)          :{}".format(data['weather'][0]['description']))
    print("Sunrise               :{}".format(time.strftime("%d %b %Y %H:%M:%S",time.localtime(data['sys']['sunrise']))))
    print("Sunset                :{}".format(time.strftime("%d %b %Y %H:%M:%S",time.localtime(data['sys']['sunset']))))
    print("------------------------------------------------")
   
    
def main():
    
    print("Weather Information")
    print("--------------------")
    location = input("Provide the City Name or the City Id   : ")

    #Check the location object to identify if its a name or city-id.
    #This is done by trying to convert using int(location) and checking if ValueError is thrown or not.
    is_string=True
    
    try:
        location = int(location)
        is_string=False
    except ValueError as v:        
        #print("Its string and value is: %s" % str_loc)
        pass

    #Now we know if City ID or Name was entered. Call the query_weather_info function passing appropriate argument.
    try:
        wdata = query_weather_info(location, is_string)
        print_required_info(wdata)
    except:
        print("Please check the input.")
        pass


if __name__=="__main__":
    main()
    


