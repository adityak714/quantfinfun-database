import logging
from typing import List

import pandas as pd

from scripts import add_entry_to_database
from scripts.stock_downloader import StockDownloader
from tables.stock_price import StockPriceDataset

# Logger Configuration
logger = logging.getLogger("test")
logFileFormatter = logging.Formatter(
    fmt=(
        f"%(levelname)s "
        f"%(asctime)s "
        f"(%(relativeCreated)d) \t "
        f"%(pathname)s; Module_Name: {__name__}; "
        f"F%(funcName)s L%(lineno)s - "
        f"%(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename="error.log")
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.INFO)
logger.addHandler(fileHandler)
logger.addHandler(logging.StreamHandler())


def get_SNP500() -> List[str]:
    tickers = pd.read_html(
        ("https://en.wikipedia.org/wiki/" "List_of_S%26P_500_companies")
    )[0]

    return list(tickers["Symbol"].iloc[:].values)


def fill_database(tickers: List[str]) -> None:
    downloader = StockDownloader()

    for ticker in tickers:
        stock_price_history = downloader.download_stocks(ticker)
        asset = ticker
        try:
            stock_history_objects = []
            for index, row in stock_price_history.iterrows():
                entry_dict = {
                    "date": index,
                    "asset": asset,
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": int(row["Volume"]),
                    "dividends": float(row["Dividends"]),
                    "stock_split": float(row["Stock Splits"]),
                }
                stock_price_entry = StockPriceDataset(**entry_dict)
                stock_history_objects.append(stock_price_entry)
            add_entry_to_database(stock_history_objects)
        except Exception as e:
            logger.error(f"{e}, {ticker}")

        print(f"Finished Populating {asset}")


if __name__ == "__main__":
    fill_database(get_SNP500())
