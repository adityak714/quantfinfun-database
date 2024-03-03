import logging

import pandas as pd
import yfinance as yf  # type: ignore

# Logger Configuration
logger = logging.getLogger("test")
logFileFormatter = logging.Formatter(
    fmt=(
        f"%(levelname)s "
        f"%(asctime)s "
        f"(%(relativeCreated)d) \t "
        f"%(pathname)s; "
        f"Module_Name: {__name__}; "
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
            tickerObj = yf.Ticker(ticker)
            tickerObjHist = tickerObj.history(period="max")
            return tickerObjHist

        # If failed then log it
        except Exception as e:
            logger.error(f"{e}, {ticker}")
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


if __name__ == "__main__":
    downloader = StockDownloader()

    downloader.download_stocks("AAPL")
