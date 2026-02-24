import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("Missing BINANCE_API_KEY or BINANCE_SECRET_KEY in .env")

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)

    def get_mark_price(self, symbol: str) -> float:
        data = self.client.futures_mark_price(symbol=symbol.upper())
        return float(data["markPrice"])

    def get_min_notional(self, symbol: str):
        info = self.client.futures_exchange_info()
        symbol_info = next(
            (item for item in info.get("symbols", []) if item.get("symbol") == symbol.upper()),
            None
        )
        if not symbol_info:
            return None

        filters = {flt.get("filterType"): flt for flt in symbol_info.get("filters", [])}

        if "NOTIONAL" in filters:
            return float(filters["NOTIONAL"].get("notional", 0) or 0)
        if "MIN_NOTIONAL" in filters:
            return float(filters["MIN_NOTIONAL"].get("notional", 0) or 0)

        return None
