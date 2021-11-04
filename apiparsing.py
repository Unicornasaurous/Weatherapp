import requests 
import json
#This is the script that sorts through and connects various API's for use in weather.py


def parsing(city, state):
    latlng = requests.get('http://open.mapquestapi.com/geocoding/v1/address?key=IGO9pUBRUuzEJBPpDmFAOqqP7eKcicUZ&location=%s,%s' % (city, state)) #Geocode API
    databulk = latlng.json()
    location = databulk['results']
    for pissboi in location:
        poop = pissboi['locations']
    for yomom in poop:
        poopindex = poop.index(yomom)
        tiger = poop[poopindex]
        reallocation = tiger['latLng']
        lat = reallocation['lat']                                                                                                                          
        lng = reallocation['lng']
        print(lat, lng)                                                                                                  #parses through json to retrieve longitude and latitude values
    response = requests.get('https://api.weather.gov/points/%s,%s' % (lat, lng))                                         #weather grid points API(takes in longitude and latitude and gives back grid points and office ID used for weather forecast )
    gridendpoints = response.json()
    context = gridendpoints['properties']
    x = context['gridX']
    y = context['gridY']
    office = context['cwa']
    print(x, y)
    print(office)                                                                                                        #parses through grid points json to retrieve grid points and weather office ID
    forecastdata = requests.get('https://api.weather.gov/gridpoints/%s/%s,%s/forecast' % (office, x, y))                 #Forecast API (Takes office id/ x and y grid points and gives back a forecast)
    forecastbulk = forecastdata.json()
    properties = forecastbulk['properties']
    periods = properties['periods']
    parsing.fore = dict()
    for index in periods:
        dayofweek = index['name']
        temperature = index['temperature']
        temperatureunit = index['temperatureUnit']
        windspeed = index['windSpeed']
        winddirection = index['windDirection']
        icon = index['icon']
        shortforecast = index['shortForecast']
        detailedforecast = index['detailedForecast']   
        parsing.fore[dayofweek] = [temperature, temperatureunit, windspeed, winddirection, icon, shortforecast, detailedforecast]  #parses through json to retrieve relevant data and then converts that data into a dict
    with open('forecast.json', 'w') as f:                                                                                         
        json.dump(parsing.fore, f, indent=2)                                                                                       #dumps dict as a json for later use in weather.py
