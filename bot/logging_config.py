import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    handler = RotatingFileHandler(
        "trading_bot.log",
        maxBytes=1_000_000,
        backupCount=3
    )
    
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
