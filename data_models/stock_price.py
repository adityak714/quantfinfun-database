from dataclasses import dataclass
from datetime import datetime


@dataclass
class StockPrice:
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
