#!/usr/bin/env python3
#get_weather.py - checks weather for a location from command line arguments

import json, requests, sys, urllib

def main():
    # check and get command line arguments
    if len(sys.argv) < 2:
        print('You need to specify location!')
        print('Usage: get_weather.py [location]')
        sys.exit()
    location = ' '.join(sys.argv[1:])
    
    # download the JSON data from OpenWeather.org's API
    url ='http://samples.openweathermap.org/data/2.5/weather?q=%s&appid=b6907d289e10d714a6e88b30761fae22' % (urllib.parse.urlencode({'q': location}))
    print('Getting data from:', url)
    response = requests.get(url)
    response.raise_for_status()
    
    # load JSON data into Python varaible.
    weatherData = json.loads(response.text)
    
    # Print weather
    print('===========================================================')
    print('Current weather in', location)
    print('Needs API token to work - will always print info for London')
    print('===========================================================\n')
    print('WEATHER\n')
    print(weatherData['weather'][0]['main'],'-', weatherData['weather'][0]['description'])
    print('\n')
    print('WIND\n')
    print('speed - ', weatherData['wind']['speed'])
    print('direction - ', weatherData['wind']['deg'], 'deg')
    print('\n')
    print('TEMPERATURE\n')
    print('temperature:', weatherData['main']['temp'], 'Max:', weatherData['main']['temp_max'], 'Min:', weatherData['main']['temp_min'])
    print('\n')
    
if __name__ == "__main__":
    main()