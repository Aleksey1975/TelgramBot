import json
import requests
from config import *

class APIException(Exception):
    ...

class WrongCarrency(APIException):
    ...

class EqualCarrency(APIException):
    ...

class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                return "<=0"
            r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}")
            total_base = round(json.loads(r.content)[keys[quote]] * amount, 2)
        except ValueError:
            return  "wrongamount"

        return  total_base

