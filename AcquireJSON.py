import requests
import json
from validateTicker import validation
from wealthSphereObjectsAndMethods import tickerDataBase, miniDataBase

def aquireJSON(ticker):
	url = "https://real-time-finance-data.p.rapidapi.com/stock-news"
	querystring = {
    "symbol": f"{ticker}:NASDAQ",  # Insert the variable here
    "language": "en"
	}
	headers = {
	"x-rapidapi-key": "a30f898b12mshfe46a686d8c6101p180ffbjsn0007e7e5c998",
	"x-rapidapi-host": "real-time-finance-data.p.rapidapi.com"
	}


	response = requests.get(url, headers=headers, params=querystring)
	jsonResponse = response.json()
	jsonLatest = jsonResponse['data']['news'][0]	


	
	headline = [
		f"Title: {jsonLatest['article_title']}",
		f"Source: {jsonLatest['source']}", 
		f"Type: Article",
		f"Time: {jsonLatest['post_time_utc']}",  
		f"URL: {jsonLatest['article_url']}",
		'COPY URL' 

	]	


	for item in headline:
		print(item)
	for i in range(3):
		print('')
	






def jsonSummary():
	listOfminDataBase = miniDataBase.returnTickers()
	if len(listOfminDataBase) > 0:
		for index in range(len(listOfminDataBase)):
			aquireJSON(listOfminDataBase[index])
	else:
		print('There is nothing in the database')
