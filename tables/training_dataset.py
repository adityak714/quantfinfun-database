from datetime import datetime
from typing import List

from sqlalchemy import ARRAY, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from tables import Base, get_attributes


class TrainingDataset(Base):
    __tablename__ = "training_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String), primary_key=True)

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)
