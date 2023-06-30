import urllib.parse
import requests

def find_coordinate(query):

    
    url=f'http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid=25e92c6dcb61edb25cf166e9d1fa07c7'
    json_data=requests.get(url).json()
    place_detail={
        "name":json_data[0]['name'],
        "data_lat":json_data[0]['lat'],
        "data_lon":json_data[0]['lon'],
        # "place":json_data[0]['state']
    }
    print(place_detail)
    print(json_data[0]['lat'])
    print(json_data[0]['lon'])

    return place_detail



