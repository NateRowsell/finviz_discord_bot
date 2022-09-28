import requests
from bs4 import BeautifulSoup

async def get_data(ticker):

    ticker = ticker.upper()

    url = "https://finviz.com/quote.ashx"

    params = {
        "t":{ticker}
    }

    headers = {
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        "accept-language":"en-US,en;q=0.9,it;q=0.8,es;q=0.7",
        "referer":"https://prerender.io/"
    }

    #retrive web page data and handle any errors
    try:
        page = requests.get(url=url,params=params,headers=headers)
    except:
        return 'There was an unexpected error parsing the web page. Please make sure the ticker is correct'
    
    soup = BeautifulSoup(page.content,'html.parser')

    #table of all data
    #if ticker does not exist the table will not exist
    try:
        table = soup.find(class_='snapshot-table2')
    except:
        return 'There was an unexpected error parsing the web page. Please make sure the ticker is correct'


    #get names and values from table
    names = table.find_all(class_='snapshot-td2-cp')
    values = table.find_all('b')

    #zip names and values together
    names_list = [name.text for name in names]
    values_list = [value.text for value in values]
    combination = list(zip(names_list,values_list))

    #set variables
    price = f"{combination[65][0]} - {combination[65][1]}"
    market_cap = f"{combination[6][0]} - {combination[6][1]}"
    volume = f"{combination[70][0]} - {combination[70][1]}"
    avg_volume = f"{combination[64][0]} - {combination[64][1]}"
    rel_volume = f"{combination[58][0]} - {combination[58][1]}"
    range_52_week = f"{combination[34][0]} - {combination[34][1]}"
    insider_own = f"{combination[3][0]} - {combination[3][1]}"
    inst_own = f"{combination[15][0]} - {combination[15][1]}"
    shs_outstand = f"{combination[4][0]} - {combination[4][1]}"
    shs_float = f"{combination[10][0]} - {combination[10][1]}"
    short_float = f"{combination[16][0]} - {combination[16][1]}"
    short_ratio = f"{combination[22][0]} - {combination[22][1]}"
    shortable = f"{combination[60][0]} - {combination[60][1]}"

    result = await f"""
        Ticker - {ticker}
        {price}
        {market_cap}
        {volume}
        {avg_volume}
        {rel_volume}
        {range_52_week}
        {insider_own}
        {inst_own}
        {shs_outstand}
        {shs_float}
        {short_float}
        {short_ratio}
        {shortable}
    """

    return result 

