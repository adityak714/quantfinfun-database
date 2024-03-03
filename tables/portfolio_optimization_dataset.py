# Create three tables for portfolio optimization. Full Dataset, Training Dataset, Testing Dataset

# Get rid of Training Dataset and benchmark dataset tables

from datetime import datetime
from typing import List

from sqlalchemy import ARRAY, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from tables import Base
from utils import get_attributes


class PortfolioOptimizationTrainingDataset(Base):
    __tablename__ = "portfolio_optimization_training_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String), primary_key=True)

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)


from tables import Base, get_attributes


class PortfolioOptimizationBenchmarkDataset(Base):
    __tablename__ = "portfolio_optimization_benchmark_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String), primary_key=True)

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)


class PortfolioOptimizationFullDataset(Base):
    __tablename__ = "portfolio_optimization_full_dataset"
    
    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String))
    
    def __repr__(self) -> str:
        return get_attributes(self)
    
    def __str__(self) -> str:
        return get_attributes(self)