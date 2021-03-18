import websocket, json, pprint
from binance.enums import *
import pandas as pd
import numpy as np
import talib

"""
Binance Documnetation for Kline return
--------------------------------------
    t: Kline start time
    T: Kline close time
    s: Symbol
    i: Interval
    f: First Trade ID
    L: Last Trade ID
    o: Open Price
    c: Close Price
    h: High price
    l: Low Price
    v: Base asset volume **
    n: Number of trades **
    x: candle closed?
    q: quote asset volume **
    V: Taker buy base asset volume
    Q: Taker buy quote asset volume
    B: Ignore

"""

# stream socket
w_socket = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'

# container for closes
closes = []
in_position = False

# message functions
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received message')

    global closes # reference the global variable closes

    # here, messages are return in json format
    json_message = json.loads(message)
    #pprint.pprint(json_message) #pretty print of candle stick

    candle = json_message['k'] # contains candle dict, k is the key
    is_candle_closed = candle['x'] # flag for closed candle
    close = candle['c'] # close value

    if is_candle_closed:
        print(f'candle closed at {close}')
        closes.append(float(close))

        # TODO: Enter strategies here
        # strategy on closing prices
        if len(closes) > 5:
            np_closes = np.array(closes)
            rsi = talib.RSI(np_closes, 5)

            print(rsi)

# initialize websocket for data stream
#TODO: wrap the data within a larger trading bot class. This way, we can apply the data, trading strategy, and execution within a single call.
ws = websocket.WebSocketApp(w_socket, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()


# class Data(object):
#
#     def __init__(self):
#         # instantiate websocket
#         self.socket = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'
#         self.closes = []
#
#         self.ws = websocket.WebSocketApp(self.socket, on_open=self.on_open, on_close=self.on_close, on_message=self.on_message)
#         self.ws.run_forever()
#
#     # message functions
#     def on_open(self, ws):
#         print('opened connection')
#
#     def on_close(self, ws):
#         print('closed connection')
#
#     def on_message(self, ws, message):
#         print('received message')
#
#         # here, messages are return in json format
#         json_message = json.loads(message)
#         pprint.pprint(json_message) #pretty print of candle stick
#
#         candle = json_message['k'] # contains candle dict, k is the key
#         is_candle_closed = candle['x'] # flag for closed candle
#         close = candle['c'] # close value
#
#         self.closes.append(close)
#
#         print(self.closes)
#
#
#     def run(self):
#         ws = websocket.WebSocketApp(self.socket, on_open=on_open, on_close=on_close, on_message=on_message)
#         ws.run_forever()
#
#     def print_test(self, message):
#         print('testing' + message)
#
#
# test_class = Data()
