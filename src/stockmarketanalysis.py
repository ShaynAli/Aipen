
import quandl
import pandas as pd
import numpy as np
import datetime

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


import pip
pip.main(["install","scipy"]);
df = quandl.get("WIKI/AMZN")
df = df[['Adj. Close']]
forecast_out = int(50) # predicting 30 days into future
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out) #  label column with data shifted 50 units up
X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)
X_forecast = X[-forecast_out:] # set X_forecast equal to last 50
X = X[:-forecast_out] # remove last 50 from X
Y= np.array(df['Prediction'])
Y = Y[:-forecast_out]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.5)
clf = LinearRegression()
clf.fit(X_train,Y_train)
# Testing
confidence = clf.score(X_test, Y_test)
print("confidence: ", confidence)
forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)
print(df.tail())