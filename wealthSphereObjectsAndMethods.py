from validateTicker import validation
import requests
class tickerDataBase:
    def __init__(self):
        self.tickerList = []
    def addTicker(self, ticker):
        if validation(ticker) != 200:
            print('Invalid Ticker')
        elif len(self.tickerList) > 10:
            print('You are limited to 10 tickers')
        elif ticker in self.tickerList:
            print('Ticker already in database')
        elif validation(ticker) == 200 and len(self.tickerList) < 10 and ticker not in self.tickerList:
            self.tickerList.append(ticker.upper())
    def removeTicker(self,ticker):
        if ticker in self.tickerList:
            self.tickerList.remove(ticker)
            print(f"{ticker.upper()} has been removed")
        elif ticker.upper() not in self.tickerList:
            print(f'{ticker.upper()} is not in your database')
    def removeAllTickers(self):
        if len(self.tickerList) > 0:
            print('Removed all tickers')
            self.tickerList.clear()
        else:
            print('There are no tickers')
    def seeTickers(self):
        if len(self.tickerList) > 0:
            for index in range(len(self.tickerList)):
                print(f"{index + 1} {self.tickerList[index]}")
        else:
            print('There is nothing in the database')
    def returnTickers(self):
        return self.tickerList
       
miniDataBase = tickerDataBase()







    
