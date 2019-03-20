import sys
import quandl
import datetime
s=input('Enter source')
yearStart = int(input('Enter a year'))
monthStart = int(input('Enter a month'))
dayStart = int(input('Enter a day'))
yearEnd = int(input('Enter a year'))
monthEnd = int(input('Enter a month'))
dayEnd = int(input('Enter a day'))
startDate = datetime.date(yearStart, monthStart, dayStart)
endDate=datetime.date(yearEnd,monthEnd,dayEnd)

def stock_price(s,startDate,endDate):

    quandl_api_key = "iJPgzXWsmJA4A-J-Hfku"
    quandl.ApiConfig.api_key = quandl_api_key


    apple = quandl.get("WIKI/" + s, start_date=startDate, end_date=endDate)

    type(apple)
    print(apple)
    return apple

def main():
    stock_price(s,startDate,endDate)
if __name__ == '__main__':
    main()


