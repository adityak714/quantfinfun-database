import os

from sqlalchemy import create_engine

from tables import Base
from tables.distribution_table import DistributionDataset  # noqa: F401
from tables.portfolio_optimization_dataset import (  # noqa: F401
    PortfolioOptimizationBenchmarkDataset,
    PortfolioOptimizationTrainingDataset,
    PortfolioOptimizationFullDataset
)
from tables.stock_price import StockPriceDataset  # noqa: F401


def main() -> None:
    engine = create_engine(str(os.getenv("DB_URL")), echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
