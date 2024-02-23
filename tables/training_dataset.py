from typing import List
from sqlalchemy import ARRAY, DateTime, String
from sqlalchemy.orm import mapped_column, Mapped
from tables import Base, get_attributes
from datetime import datetime


class TrainingDataset(Base):
    __tablename__ = "training_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String), primary_key=True)

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)
