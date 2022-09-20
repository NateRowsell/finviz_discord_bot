import requests
import json 


async def get_data(ticker):
    url = "https://finviz.com/api/quote.ashx"

    params = {
        "aftermarket":"true",
        "instrument":"stock",
        "patterns":"true",
        "premarket":"true",
        "rev":"1663717091905",
        "ticker":{ticker},
        "timeframe":"d",
        "type":"new",
    }
