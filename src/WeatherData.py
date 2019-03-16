
# #A very general generation of weather data from xarray
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import pip
# pip.main(['install','xarray'])
# np.random.seed(500)
# import xarray as xr
#
# times = pd.date_range('2018-01-01', '2019-01-01', name='time')
# annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))
#
# base = 10 + 15 * annual_cycle.reshape(-1, 1)
# tmin_values = base + 3 * np.random.randn(annual_cycle.size, 2)
# tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 2)
#
# ds = xr.Dataset({'tmin': (('time', 'location'), tmin_values),
#                  'tmax': (('time', 'location'), tmax_values)},
#                 {'time': times, 'location': ['USA','CA']})
# print(ds)
# df = ds.to_dataframe()
# print(df.head())
# print(df.tail())
# print(df.describe())
# ds.mean(dim='location').to_dataframe().plot()
# plt.show()

# # import pip
# # pip.main(["install","pyowm"])
# import pyowm
# owm=pyowm.OWM('edd4e6cc68d1e08f7c62857a0a78b27f')
# lo=owm.three_hours_forecast('London,CA')
# print(lo.get_weather_at(timeobject='2018-01-01 16:00:01'))

# import pip
# pip.main(['install','darkskylib'])
# pip.main(['install','git+git://github.com/locustio/locust.git@master#egg=locustio'])
# from darksky import forecast
# from datetime import date, timedelta
#
# CANADA = 42.9849, 81.2453
#
# weekday = date.today()
# with forecast('0a99a407f5d24d060322e6d60996d95f', *CANADA) as canada:
#     print(canada.daily.summary, end='\n---\n')
#     for day in canada.daily:
#         day = dict(day = date.strftime(weekday, '%a'),
#                    sum = day.summary,
#                    tempMin = day.temperatureMin,
#                    tempMax = day.temperatureMax
#                    )
#         print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
#         weekday += timedelta(days=1)
#         canada.refresh()
#         print(canada.time, canada.temperature, len(canada.hourly))
# ,error_bad_lines=False
# encoding = "utf-8",error_bad_lines=False

# import csv
#
# with open('weatherHistory.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(row)
#
# csvFile.close()
import numpy as np
import pandas as pd
# myfile = np.loadtxt('JaipurFinalCleanData.csv', delimiter=',',dtype=object)
df = pd.read_csv('JaipurFinalCleanData.csv').set_index('date')
# myfile = np.array(myfile[1:], dtype=object)
# print(myfile)
print(df)