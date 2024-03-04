"""
Models defining the data returned by the
stock_price_table
"""

__module__ = "stock_price_model"
__author__ = "Mohd Sadiq"
__version__ = "v0.1"

from dataclasses import dataclass
from datetime import datetime


@dataclass
class StockPrice:  # pylint: disable=too-many-instance-attributes
    """Dataclass for stock price table"""

    date: datetime
    asset: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dividends: float
    stock_split: float
    capital_gains: float
