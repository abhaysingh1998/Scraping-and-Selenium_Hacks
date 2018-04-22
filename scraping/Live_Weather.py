import requests
from pprint import pprint

def view_weather() :

    x = raw_input("Enter the Place : ")
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + x + '&APPID=a4c44b228e720ea728b757f3aa754c06'

    r = requests.get(url)
    data_json = r.json()

    #print data_json
    print "Current Weather : " + str(data_json['main']['temp'] - 273)
    print "Maximum Weather : " + str(data_json['main']['temp_max'] - 273)
    print "Minimum Weather : " + str(data_json['main']['temp_min'] - 273)
    print "Wind Speed: " + str(data_json['wind']['speed']) + "m/s"
    print "Humidity : " + str(data_json['main']['humidity']) + "%"

view_weather()
