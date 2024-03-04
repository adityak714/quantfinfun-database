"""
 Definition of three tables for portfolio optimization.
 Full Dataset, Training Dataset, Testing Dataset
"""

__author__="Mohd Sadiq"
__version__="v0.1"
__module__="portfolio_optimization_dataset"

from datetime import datetime
from typing import List, Tuple

from sqlalchemy import ARRAY, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from tables import Base
from utils import get_attributes


class PortfolioOptimizationTrainingDataset(Base):
    """Defition of portfolio_optimization_training_dataset table"""
    __tablename__ = "portfolio_optimization_training_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[Tuple[str]] = mapped_column(
        ARRAY(String), primary_key=True
    )

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)


class PortfolioOptimizationBenchmarkDataset(Base):
    """Defition of portfolio_optimization_benchmark_dataset table"""
    __tablename__ = "portfolio_optimization_benchmark_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[Tuple[str]] = mapped_column(
        ARRAY(String), primary_key=True
    )

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)


class PortfolioOptimizationFullDataset(Base):
    """Defition of portfolio_optimization_full_dataset table"""
    __tablename__ = "portfolio_optimization_full_dataset"

    date: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String))

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)
