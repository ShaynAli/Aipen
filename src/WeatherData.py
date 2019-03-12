
#A very general generation of weather data from xarray

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pip
pip.main(['install','xarray'])
np.random.seed(500)
import xarray as xr

times = pd.date_range('2018-01-01', '2019-01-01', name='time')
annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

base = 10 + 15 * annual_cycle.reshape(-1, 1)
tmin_values = base + 3 * np.random.randn(annual_cycle.size, 2)
tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 2)

ds = xr.Dataset({'tmin': (('time', 'location'), tmin_values),
                 'tmax': (('time', 'location'), tmax_values)},
                {'time': times, 'location': ['USA','CA']})
print(ds)
df = ds.to_dataframe()
print(df.head())
print(df.tail())
print(df.describe())
ds.mean(dim='location').to_dataframe().plot()
plt.show()
