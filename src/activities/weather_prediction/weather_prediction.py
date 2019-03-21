from activities.activities import MachineLearningActivity
import pandas as pd
from _datetime import date
import pdb
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd2
import csv
import data_utils.weather_data
import pdb

df = pd2.read_csv('../../../data/data_monthly_rainfall.csv', delimiter=',')
df2 = df['Year'].values[0]
df3 = df['StationIndex'].values[0]
class HungaryWeatherPrediction(MachineLearningActivity):



    df = pd2.read_csv('../../../data/data_monthly_rainfall.csv', delimiter=',')
    df2 = df['Year']
    df3 = df['StationIndex']
    years = [years for years in df.iteritems()]
    stationIndex = [stationIndex for stationIndex in df.iteritems()]

# print(df2)
# print(df3)

    def __init__(self, years=df2, stationIndex=df3):
        # pdb.set_trace()
        self.years = df2
        self.stationIndex = df3


    @property
    def x_shape(self):
        return len({self.years})


    @property
    def y_shape(self):
        return len({self.stationIndex})

    def next_data(self):
        from random import choice
        year = choice(HungaryWeatherPrediction.years)
        month = choice(HungaryWeatherPrediction.stationIndex)

        rainfall_data = []

        for year in df.iterrows():
            print(f'Getting rain data for {year}')
            rainfall_data.append(self.get_rainfall(year, rainfall_data))
        rainfall_data_supply = []
        for stationIndex in df.iterrows():
            print(f'Getting rain data for {stationIndex}')
            rainfall_data_supply.append(self.get_rainfall(year,stationIndex))

        try:
            years = pd.concat(rainfall_data)
            stationIndex = pd.concat(rainfall_data_supply)
        except ValueError:
            return self.next_data()

        return years, rainfall_data


    def get_rainfall(self, year, stationIndex):
        return df.info()


if __name__ == '__main__':
    activity = HungaryWeatherPrediction()
    data = [activity.next_data() for _ in range(10)]
    pdb.set_trace()
