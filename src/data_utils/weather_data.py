
import pandas as pd
df = pd.read_csv("../../data/weatherHistory.csv",delimiter=',')
df2=pd.read_csv("../../data/data_monthly_rainfall.csv",delimiter=',')
# meanTemp=df['Temperature (C)'].mean()
print("----------Szeged Hungary----------")
print(df)
print("----------Bangladesh----------")
print(df2)
# print('Mean temp: ' + str(meanTemp))
