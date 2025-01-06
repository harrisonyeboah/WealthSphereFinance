import requests

def validation(ticker):
    url = "https://real-time-finance-data.p.rapidapi.com/stock-news"
    querystring = {
        "symbol": f"{ticker}:NASDAQ", 
        "language": "en"
    }
    headers = {
	"x-rapidapi-key": "a30f898b12mshfe46a686d8c6101p180ffbjsn0007e7e5c998",
	"x-rapidapi-host": "real-time-finance-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    code = response.status_code
    return code


