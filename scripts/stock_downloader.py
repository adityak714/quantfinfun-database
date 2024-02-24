import yfinance as yf
import pandas as pd
import logging
from tqdm import tqdm

# IMPORTS #

# Logger Configuration
logger = logging.getLogger("test")
logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s; Module_Name: {__name__}; F%(funcName)s L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename='error.log')
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.INFO)
logger.addHandler(fileHandler)


class StockDownloader:
    '''
        Class
            Downloads stock history
            
        Methods:
            download_stocks:
                Args:
                    tickers (str): Ticker of the asset in question
                
    '''
    
    def download_stocks(self,ticker):
        
        '''
            Method
                Download Stock History
                
            Args:
                ticker (list): List of all tickers
                
        '''
        
        
        # Start Download for tickers
        
        # Try downloading
        try:
            tickerObj = yf.Ticker(ticker)
            tickerObjHist = tickerObj.history(period="max")
            return tickerObjHist            
        
        # If failed then log it
        except Exception as e:
            logger.error(f'{e}, {ticker}')


if __name__=='__main__':
    downloader = StockDownloader()
    
    downloader.download_stocks('AAPL')