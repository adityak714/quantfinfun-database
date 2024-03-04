"""
    This script is responsible for populating the datasets
    that would be required for training and validating our models
"""

__author__ = "Mohd Sadiq"
__module__ = "populate dataset"
__version__ = "v0.1"

import os
import random

import sqlalchemy as db

from scripts import add_entry_to_database
from tables.portfolio_optimization_dataset import (
    PortfolioOptimizationBenchmarkDataset,
    PortfolioOptimizationFullDataset, PortfolioOptimizationTrainingDataset)
from utils import build_logger

# Logger Configuration
error_logger, console_logger = build_logger(__module__)


def populate_portfolio_optimization_dataset() -> None:
    """
    This script is responsible for populating the Full Dataset
    """
    engine = db.create_engine(str(os.getenv("DB_URL")))

    connection = engine.connect()

    metadata = db.MetaData()

    stock_price_data = db.Table(
        "stock_price_dataset", metadata, autoload_with=engine
    )

    unique_dates_query = db.select(
        stock_price_data.columns.date.distinct()
    ).order_by(db.desc(stock_price_data.columns.date))

    unique_date_result_set = connection.execute(
        unique_dates_query
    ).fetchall()

    for date_entry in unique_date_result_set:
        date = date_entry[0]
        portfolio_optimization_dict = {"date": date, "assets": []}

        sub_query = (
            db.select(
                stock_price_data.columns.asset.distinct().label("asset"),
                db.func.count(  # pylint: disable=not-callable
                    stock_price_data.columns.asset
                ).label(  # pylint: disable=not-callable
                    "asset_count"
                ),
            )
            .where(stock_price_data.columns.date < date)
            .group_by(stock_price_data.columns.asset)
        )

        main_query = db.select(
            sub_query.subquery().columns.asset.distinct()
        ).where(sub_query.subquery().columns.asset_count >= 180)

        result_set = connection.execute(main_query).fetchall()

        portfolio_optimization_dict["assets"] = [
            asset[0] for asset in result_set
        ]

        portfolio_optimization_dataset_entry = (
            PortfolioOptimizationFullDataset(**portfolio_optimization_dict)
        )

        try:
            add_entry_to_database([portfolio_optimization_dataset_entry])
            console_logger.info("Added entry for date %s", date)
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error(
                "Errored while adding entry. Error: %s", error
            )


def populate_portfolio_optimization_training_dataset() -> None:
    """This script is responsible for populating the training dataset"""
    engine = db.create_engine(str(os.getenv("DB_URL")))

    connection = engine.connect()

    metadata = db.MetaData()

    portfolio_optimization_dataset = db.Table(
        "portfolio_optimization_full_dataset",
        metadata,
        autoload_with=engine,
    )

    query = db.select(portfolio_optimization_dataset)

    result_proxy = connection.execution_options(
        stream_results=True
    ).execute(query)

    while chunk := result_proxy.fetchmany(1000):
        training_dataset_entries = []
        for row in chunk:
            date = row[0]
            if len(row[1]) >= 30:
                for _ in range(10):
                    asset_list = tuple(random.sample(row[1], 20))
                    training_dataset_entry_dict = {
                        "date": date,
                        "assets": asset_list,
                    }
                    training_dataset_entry = (
                        PortfolioOptimizationTrainingDataset(
                            **training_dataset_entry_dict
                        )
                    )
                    training_dataset_entries.append(training_dataset_entry)
        try:
            add_entry_to_database(training_dataset_entries)
            console_logger.info("Added a chunk of 1000 dates successfully")
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error(
                "Errored while populating the 1000 dates. Error:%s", error
            )


def populate_portfolio_optimization_benchmark_dataset() -> None:
    """
    This script is responsible for populating the benchmark dataset
    """
    engine = db.create_engine(str(os.getenv("DB_URL")))

    connection = engine.connect()

    metadata = db.MetaData()

    portfolio_optimization_dataset = db.Table(
        "portfolio_optimization_full_dataset",
        metadata,
        autoload_with=engine,
    )

    query = db.select(portfolio_optimization_dataset)

    result_proxy = connection.execution_options(
        stream_results=True
    ).execute(query)

    while chunk := result_proxy.fetchmany(1000):
        training_dataset_entries = []
        for row in chunk:
            date = row[0]
            if len(row[1]) >= 30:
                for _ in range(2):
                    asset_list = tuple(random.sample(row[1], 20))
                    training_dataset_entry_dict = {
                        "date": date,
                        "assets": asset_list,
                    }
                    training_dataset_entry = (
                        PortfolioOptimizationBenchmarkDataset(
                            **training_dataset_entry_dict
                        )
                    )
                    training_dataset_entries.append(training_dataset_entry)
        try:
            add_entry_to_database(training_dataset_entries)
            console_logger.info("Added a chunk of 1000 dates successfully")
        except Exception as error:  # pylint: disable=broad-except
            error_logger.error(
                "Errored while populating the 1000 dates. Error:%s", error
            )


if __name__ == "__main__":
    populate_portfolio_optimization_benchmark_dataset()
