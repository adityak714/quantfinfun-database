from sqlalchemy import Column, DateTime, ARRAY, String, Float, Integer

from tables import get_attributes, Base


class StockPriceDataset(Base):
    __tablename__ = "stock_price_dataset"
    
    date = Column(DateTime, primary_key=True)
    asset = Column(String, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    dividends = Column(Float)
    stock_split = Column(Float)
    capital_gains = Column(Float)
    
    def __repr__(self) -> None:
        return get_attributes(self)
    
    def __str__(self) -> None:
        return get_attributes(self)