from datetime import datetime
import meteostat
import requests
import pandas as pd


def get_weather(location, year):
    start = datetime(year, 4, 1)
    end = datetime(year, 9, 30)

    respons = requests.get(
        f'https://api.opencagedata.com/geocode/v1/json?q={location}&key=555c1da178f94aa4897b0393225d0776&language=en&pretty=1')
    response = respons.json()

    longlat = meteostat.Point(
        response['results'][1]['geometry']['lat'], response['results'][1]['geometry']['lng'])

    data = meteostat.Monthly(loc=longlat, start=start, end=end)
    data = data.fetch()
    df = data.iloc[:, :4]
    df = df.stack().reset_index()
    df = df.T
    return df

get_weather('Pauillac', 2020)

