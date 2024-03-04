"""
This script is responsible for downloading the stock price
information
"""

__module__ = "stock_downloader"
__author__ = "Mohd Sadiq"
__version__ = "v0.1"

import pandas as pd
import yfinance as yf  # type: ignore

from utils import build_logger, get_attributes

# Logger Configuration
error_logger, console_logger = build_logger(__module__)


class StockDownloader:
    """
    Class
        Downloads stock history

    Methods:
        download_stocks:
            Args:
                tickers (str): Ticker of the asset in question

    """

    def download_stocks(self, ticker: str) -> pd.DataFrame:

        """
        Method
            Download Stock History

        Args:
            ticker (str): ticker code

        Output:
            (pd.DataFrame) : pandas dataframe that has the
                            full history of the stock

        """

        # Try downloading
        try:
            ticker_obj = yf.Ticker(ticker)
            ticker_obj_hist = ticker_obj.history(period="max")
            return ticker_obj_hist

        # If failed then log it
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error("%s, %s", error, ticker)
        df3 = pd.DataFrame(
            columns=[
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Dividends",
                "Stock Splits",
            ]
        )
        return df3

    def __str__(self) -> str:
        return get_attributes(self)

    def __repr__(self) -> str:
        return get_attributes(self)


if __name__ == "__main__":
    downloader = StockDownloader()

    downloader.download_stocks("AAPL")
