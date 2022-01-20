'''

@author: 
Keys: date - timestamp, debt ratio, loans[loans of each currency, total in USDT], purchasing power[assets{each coin}, total = assets+ loans], equity[realized value right now: assets - liabilities, realized value at market stop]
'''
key = 'yourkey'
secret = 'yoursecret'
passphrase = 'yourpassphrase'#
is_sandbox = True
url = 'https://openapi-sandbox.kucoin.com'

import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient
from kucoin.client import*

ws_token = GetToken(key, secret, passphrase, is_sandbox, url)
token = ws_token.get_ws_token(is_private=True)


async def main():
    async def deal_msg(msg):
            #print(msg["data"]["debtRatio"])
            print(msg["price"])
            
    # is public
    # client = WsToken()
    #is private
    client = WsToken(key, secret, passphrase, is_sandbox)
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=True)
    await ws_client.subscribe('/api/v1/market/histories?symbol=ETH-USDT')
    #await ws_client.subscribe('/margin/position')
    while True:
        await asyncio.sleep(0)
        
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    

#Uncomment for more functionality
#from datetime  import *
#import uuid, json, csv
# def get_info():
    # #from datetime import 
    # client = User(key, secret, passphrase, is_sandbox)
    # market = MarketData(key, secret, passphrase, is_sandbox, url)
    # margin = MarginData(key, secret, passphrase, is_sandbox, url)
    #
    # time = (datetime.now().strftime("%H:%M:%S")+ '|' + str(date.today()))
    # print (time)
    # debtRatio = str(float(margin.get_margin_account()['debtRatio']) * 100) + '%'
    # print (debtRatio)
    # print(json.dumps(margin.get_margin_account(),indent = 1))
    # return 
    #
# get_info()
# # client.inner_transfer("USDT", "main", "margin", 1000, 1)
#
# # margin = MarginData(key, secret, passphrase, is_sandbox, url)
# # print (json.dumps(margin.get_margin_account(),indent=1))
#
# # client = Trade(key, secret, passphrase, is_sandbox, url)
# # order_id = client.create_market_order('BTC-USDT', 'buy', size='0.01',type = 'market')
# # print(order_id)
