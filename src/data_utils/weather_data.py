import pandas as pd


def weatherData():
    df = pd.read_csv("../../data/weatherHistory.csv", delimiter=',')
    df2 = pd.read_csv("../../data/data_monthly_rainfall.csv", delimiter=',')
    # meanTemp=df['Temperature (C)'].mean()

    print("----------Szeged Hungary----------")
    print(df)
    print("----------Bangladesh----------")
    print(df2)
    print(df.columns)





def main():
    weatherData()

if __name__ == '__main__':
    main()