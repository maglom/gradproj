from datetime import datetime
import meteostat
import requests
import pandas as pd


def get_weather_monthly(year):
    start = datetime(year, 4, 1)
    end = datetime(year, 9, 30)

    # respons = requests.get(
    #     f'https://api.opencagedata.com/geocode/v1/json?q={location}&key=555c1da178f94aa4897b0393225d0776&language=en&pretty=1',timeout=10)
    # response = respons.json()

    # longlat = meteostat.Point(
    #     response['results'][1]['geometry']['lat'], response['results'][1]['geometry']['lng'])
    
    longlat = meteostat.Point(
        49.91977295744827, 7.063145379315835
        )

    data = meteostat.Monthly(loc=longlat, start=start, end=end)
    data = data.fetch()
    df = data[[x for x in data.columns if x in ['tavg', 'tmin', 'tmax', 'prcp']]]
    df = df.stack().reset_index()
    df = df.T
    return df


def get_weather_daily(year):
    start = datetime(year, 4, 1)
    end = datetime(year, 9, 30)

    # respons = requests.get(
    #     f'https://api.opencagedata.com/geocode/v1/json?q={location}&key=555c1da178f94aa4897b0393225d0776&language=en&pretty=1',timeout=10)
    # response = respons.json()

    # longlat = meteostat.Point(
    #     response['results'][1]['geometry']['lat'], response['results'][1]['geometry']['lng'])
    
    longlat = meteostat.Point(
        44.864812831248145, -0.5748540613726731
        )

    data = meteostat.Daily(loc=longlat, start=start, end=end)
    data = data.fetch()
    df = data[[x for x in data.columns if x in ['tavg', 'tmin', 'tmax', 'prcp']]]
    df = df.stack().reset_index()
    df = df.T
    return df

def make_weather_df(interval, winedata_path):
    if interval == 'daily':
        weather_columns = get_weather_daily(2000)
        df_weather = pd.DataFrame(columns=weather_columns.columns)
            
        df = pd.read_csv(winedata_path)

        for index, row in df.iterrows():
            weather = get_weather_daily(row['Year']).iloc[2,:]
            df_weather = df_weather.append(weather)
            print(df_weather.tail(2))
            print(df_weather.shape)
        return df_weather
    elif interval == 'monthly':
        weather_columns = get_weather_monthly(2000)
        df_weather = pd.DataFrame(columns=weather_columns.columns)
            
        df = pd.read_csv(winedata_path)

        for index, row in df.iterrows():
            year = int(row['Year'])
            print(isinstance(year,int))
            weather = get_weather_monthly(int(year)).iloc[2,:]
            df_weather = df_weather.append(weather)
            print(df_weather.tail(2))
            print(df_weather.shape)
        return df_weather

