import argparse
from bot.orders import create_order
from bot.validators import *
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        logger.info(f"Order Request: {vars(args)}")

        response = create_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        logger.info(f"Order Response: {response}")

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print("\n===== RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("\nOrder placed successfully.")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print(f"\nOrder failed: {str(e)}")


if __name__ == "__main__":
    main()