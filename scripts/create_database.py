"""
    Script to create the tables in the database
"""

import os

from sqlalchemy import create_engine

from tables import Base
from tables.distribution_table import \
    DistributionDataset  # noqa: F401  # pylint: disable=unused-import
from tables.portfolio_optimization_dataset import (  # noqa: F401,E501  # pylint: disable=unused-import
    PortfolioOptimizationBenchmarkDataset,
    PortfolioOptimizationFullDataset, PortfolioOptimizationTrainingDataset)
from tables.stock_price import \
    StockPriceDataset  # noqa: F401  # pylint: disable=unused-import


def main() -> None:
    """
    This function is responsible for creating the tables in the database
    """
    engine = create_engine(str(os.getenv("DB_URL")), echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
