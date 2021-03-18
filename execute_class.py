import robin_stocks as r
import robin_stocks.helper as helper
import json
import pandas as pd
import os

"""
Robin stocks crypto order types
--------------------------------

buy
----
buy_crypto_by_price - done
buy_crpyto_by_quantity - done
buy_crypto_limit -
buy_crypto_limit_by_price

sell
-----
sell_crypto_by_price
sell_crypto_by_quantity
sell_crypto_limit
sell_crypto_limit_by_price
"""

class Robinhood(object):

    def __init__(self, username, password, store_session):
        """
        Trade execution API for robinhood.
        """
        # user credentials
        self.username = username
        self.password = password
        self.store_session = store_session

        # login
        self.login = r.authentication.login(self.username, self.password, self.store_session)

    # check crypto position
    #TODO: determine whether the 'quantity_held_for_buy' & 'quantityheld_for_sell' is dynamic based on pending positions as well
    def get_crypto_positions(self, info=None):
        """
        Extracts crypto portfolio and positions

            Available columns (after pandas)
            1. quantity
            2. quantity_available
            3. currency.code (crypto ticker)
        """
        positions = r.crypto.get_crypto_positions(info=None)
        return positions

    """
    Robinhood buy/sell methods
    """
    # buy side robinhood methods
    def order_buy_crypto_by_price(self, symbol, amountInDollars):
        self = r.order_buy_crypto_by_price(symbol, amountInDollars)

    def order_buy_crypto_by_quantity(self, symbol, quantity):
        self = r.order_buy_crypto_by_quantity(symbol, quantity)

    def order_buy_crypto_limit(self, symbol, quantity, limitPrice):
        self = r.order_buy_crypto_limit(symbol, quantity, limitPrice)

    def order_buy_crypto_limit_by_price(self, symbol, amountInDollars, limitPrice):
        self = r.order_buy_crypto_limit_by_price(symbol, amountInDollars, limitPrice)

    # sell side robinhood methods
    def order_sell_crypto_by_price(self, symbol, amountInDollars):
        self = r.order_sell_crypto_by_price(symbol, amountInDollars)

    def order_sell_crypto_by_quantity(self, symbol, quantity):
        self = r.order_sell_crypto_by_quantity(symbol, quantity)

    def order_sell_crypto_limit(self, symbol, quantity, limitPrice):
        self = r.order_sell_crypto_limit(symbol, quantity, limitePrice)

    def order_sell_crypto_limit_by_price(self, symbol, quantity, limitPrice):
        self = r.order_sell_crypto_limit_by_price(symbol, quantity, limitPrice)


# ------------------------------------------------------------------------------
"""
Test robinhood class
"""
rh_username = os.getenv('rh_user')
rh_password = os.getenv('rh_pw')

rh_instance = Robinhood(username=rh_username, password=rh_password, store_session=True)
rh_instance.login['access_token']
crypto_data = rh_instance.get_crypto_positions(info=None)
pd.json_normalize(crypto_data)

# execute trade
rh_instance.order_buy_crypto_by_price(symbol='BTC', amountInDollars=1)

# Checkpoint: as of 1/31/2021, this robinhood class is functional
