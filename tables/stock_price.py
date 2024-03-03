from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from tables import Base
from utils import get_attributes


class StockPriceDataset(Base):
    __tablename__ = "stock_price_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    asset: Mapped[str] = mapped_column(String, primary_key=True)
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[int] = mapped_column(Integer)
    dividends: Mapped[float] = mapped_column(Float)
    stock_split: Mapped[float] = mapped_column(Float)

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)
