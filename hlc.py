from websocket import create_connection
import datetime
import json

test_key = 'E3BB976B-2C70-4803-A40D-D4B357BE4CDF'

class CoinAPIv1_subscribe(object):
  def __init__(self, apikey):
    self.type = "hello"
    self.apikey = apikey
    self.heartbeat = True
    self.subscribe_data_type = ["trade", "quote", "book20"]

ws = create_connection("wss://ws.coinapi.io/v1")
sub = CoinAPIv1_subscribe(test_key);
ws.send(json.dumps(sub.__dict__))
while True:
  msg =  ws.recv()
  print(msg);
ws.close()
