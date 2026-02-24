from bot.client import BinanceFuturesClient

def create_order(symbol, side, order_type, quantity, price=None):
    client = BinanceFuturesClient()
    symbol = symbol.upper()

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "newOrderRespType": "RESULT",
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    # Prevent avoidable Binance rejection (e.g., code -4164) by validating notional first.
    effective_price = float(price) if order_type == "LIMIT" else client.get_mark_price(symbol)
    min_notional = client.get_min_notional(symbol) or 100.0
    order_notional = float(quantity) * effective_price

    if order_notional < min_notional:
        min_quantity = min_notional / effective_price
        raise ValueError(
            f"Order notional too small ({order_notional:.4f}). "
            f"Minimum required is {min_notional:.4f}. "
            f"Use quantity >= {min_quantity:.6f} for {symbol} at price {effective_price:.4f}."
        )

    return client.place_order(**params)
