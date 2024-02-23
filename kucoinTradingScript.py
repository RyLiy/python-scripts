# Import necessary libraries
import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient

# Define API credentials
key = 'yourkey'
secret = 'yoursecret'
passphrase = 'yourpassphrase'
is_sandbox = True
url = 'https://openapi-sandbox.kucoin.com'

# Function to process incoming messages
async def main():
    async def deal_msg(msg):
        # Print the price from the incoming message
        print(msg["data"]["price"])
        
    # Initialize WebSocket token
    ws_token = WsToken(key, secret, passphrase, is_sandbox, url)
    token = ws_token.get_ws_token(is_private=True)

    # Initialize WebSocket client
    client = WsToken(key, secret, passphrase, is_sandbox)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=True)
    
    # Subscribe to market histories for ETH-USDT pair
    await ws_client.subscribe('/api/v1/market/histories?symbol=ETH-USDT')

    # Keep the event loop running
    while True:
        await asyncio.sleep(0)

# Run the main function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
