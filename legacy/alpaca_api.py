import alpaca_trade_api as tradeapi


import json

with open('keys.json') as f_in:
	f_str = f_in.read()
	keys_dir = json.loads(f_str)['alpaca']


api = tradeapi.REST(keys_dir['api_key_id'], keys_dir['secret_key'], base_url=keys_dir['endpoint']) # or use ENV Vars shown below
account = api.get_account()


#aapl_position = api.get_position('AAPL')
#print(appl_position)


aapl_asset = api.get_asset('GOOGL')
print(aapl_asset)
# Submit a market order to buy 1 share of Apple at market price
api.submit_order(
    symbol='GOOGL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='fok'
)


print(api.list_positions())

