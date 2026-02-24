# Trading Bot (Binance Futures Testnet)

A simple Python CLI bot to place Binance Futures Testnet orders (`MARKET` and `LIMIT`) from the command line.

## Features
- Places Binance Futures Testnet orders via `python-binance`
- Supports `BUY` and `SELL`
- Supports `MARKET` and `LIMIT` order types
- Input validation for side, type, quantity, and limit price
- Rotating file logs in `trading_bot.log`

## Project Structure
- `cli.py` - command-line entry point
- `bot/client.py` - Binance testnet client wrapper
- `bot/orders.py` - order payload builder and submitter
- `bot/validators.py` - CLI input validation
- `bot/logging_config.py` - rotating logger setup

## Requirements
- Python 3.10+
- Binance Futures Testnet API credentials

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration
Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
```

Note: This project uses Binance **Futures Testnet** endpoint:
`https://testnet.binancefuture.com/fapi`

## Usage
Basic command:

```bash
python cli.py --symbol SYMBOL --side BUY_OR_SELL --type MARKET_OR_LIMIT --quantity QTY [--price PRICE]
```

### Example: MARKET order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Example: LIMIT order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

## Output
On success, the CLI prints an order summary including:
- Symbol
- Side
- Type
- Quantity
- Order ID
- Status
- Executed quantity
- Average price (if available)

Errors are printed to console and logged to `trading_bot.log`.

## Logging
Logs are written to:
- `trading_bot.log`

Log rotation settings:
- Max size: `1,000,000` bytes
- Backups kept: `3`

## Notes
- `LIMIT` orders require `--price`.
- `MARKET` orders ignore `--price`.
- This bot is testnet-only by default (`testnet=True`).

## Security
Your `.env` currently contains real-looking API keys. Rotate/revoke them if they were exposed, and never commit secrets to source control.
