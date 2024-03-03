__script_name__ = "populate dataset"

import logging
import os

import sqlalchemy as db
import random
from scripts import add_entry_to_database
from tables.portfolio_optimization_dataset import \
    PortfolioOptimizationTrainingDataset
from tables.portfolio_optimization_dataset import \
    PortfolioOptimizationFullDataset
from tables.portfolio_optimization_dataset import \
    PortfolioOptimizationBenchmarkDataset

# Logger Configuration
logFileFormatter = logging.Formatter(
    fmt=(
        f"%(levelname)s "
        f"%(asctime)s "
        f"(%(relativeCreated)d) \t "
        f"%(pathname)s; "
        f"Module_Name: {__name__}; "
        f"%(funcName)s L%(lineno)s - "
        f"%(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S",
)

error_logger = logging.getLogger("file logger")
fileHandler = logging.FileHandler(filename=f"{__script_name__}_error.log")
fileHandler.setFormatter(logFileFormatter)
error_logger.addHandler(fileHandler)

console_logger = logging.getLogger("console logger")
console = logging.StreamHandler()
console.setFormatter(logFileFormatter)
console_logger.addHandler(console)


error_logger.setLevel(level=logging.INFO)
console_logger.setLevel(level=logging.INFO)


# Connect to the Database


def populate_portfolio_optimization_dataset():

    engine = db.create_engine(os.getenv("DB_URL"))

    connection = engine.connect()

    metadata = db.MetaData()

    stock_price_data = db.Table(
        "stock_price_dataset", metadata, autoload_with=engine
    )

    unique_dates_query = db.select(
        stock_price_data.columns.date.distinct()
    ).order_by(db.desc(stock_price_data.columns.date))

    unique_dates_result_proxy = connection.execute(unique_dates_query)
    unique_date_result_set = unique_dates_result_proxy.fetchall()

    for date_entry in unique_date_result_set:
        date = date_entry[0]
        portfolio_optimization_dict = {"date": date, "assets": []}

        sub_query = (
            db.select(
                stock_price_data.columns.asset.distinct().label("asset"),
                db.func.count(stock_price_data.columns.asset).label(
                    "asset_count"
                ),
            )
            .where(stock_price_data.columns.date < date)
            .group_by(stock_price_data.columns.asset)
        )

        main_query = db.select(
            sub_query.subquery().columns.asset.distinct()
        ).where(sub_query.subquery().columns.asset_count >= 180)

        result_proxy = connection.execute(main_query)

        result_set = result_proxy.fetchall()

        assets = [asset[0] for asset in result_set]

        portfolio_optimization_dict["assets"] = assets

        portfolio_optimization_dataset_entry = (
            PortfolioOptimizationFullDataset(**portfolio_optimization_dict)
        )

        try:
            add_entry_to_database([portfolio_optimization_dataset_entry])
            console_logger.info(f"Added entry for date {date}")
        except Exception as e:
            error_logger.error(f"Errored while adding entry. Error: {e}")


def populate_portfolio_optimization_training_dataset():
    engine = db.create_engine(os.getenv("DB_URL"))

    connection = engine.connect()

    metadata = db.MetaData()
    
    portfolio_optimization_dataset = db.Table(
        "portfolio_optimization_full_dataset", metadata, autoload_with=engine
    )
    
    query = db.select(portfolio_optimization_dataset)
    
    result_proxy = connection.execution_options(stream_results=True).execute(query)
    
    while chunk:=result_proxy.fetchmany(1000):
        training_dataset_entries = []
        for row in chunk:
            date = row[0]
            if len(row[1])>=30:
                for i in range(10):
                    asset_list = tuple(random.sample(row[1],20))
                    training_dataset_entry_dict = {'date':date, 'assets':asset_list}
                    training_dataset_entry = PortfolioOptimizationTrainingDataset(**training_dataset_entry_dict)
                    training_dataset_entries.append(training_dataset_entry)
        try:
            add_entry_to_database(training_dataset_entries)
            console_logger.info("Added a chunk of 1000 dates successfully")
        except Exception as e:
            error_logger.error(f"Errored while populating the 1000 dates. Error:{e}")


def populate_portfolio_optimization_benchmark_dataset():
    engine = db.create_engine(os.getenv("DB_URL"))

    connection = engine.connect()

    metadata = db.MetaData()
    
    portfolio_optimization_dataset = db.Table(
        "portfolio_optimization_full_dataset", metadata, autoload_with=engine
    )
    
    query = db.select(portfolio_optimization_dataset)
    
    result_proxy = connection.execution_options(stream_results=True).execute(query)
    
    while chunk:=result_proxy.fetchmany(1000):
        training_dataset_entries = []
        for row in chunk:
            date = row[0]
            if len(row[1])>=30:
                for i in range(2):
                    asset_list = tuple(random.sample(row[1],20))
                    training_dataset_entry_dict = {'date':date, 'assets':asset_list}
                    training_dataset_entry = PortfolioOptimizationBenchmarkDataset(**training_dataset_entry_dict)
                    training_dataset_entries.append(training_dataset_entry)
        try:
            add_entry_to_database(training_dataset_entries)
            console_logger.info("Added a chunk of 1000 dates successfully")
        except Exception as e:
            error_logger.error(f"Errored while populating the 1000 dates. Error:{e}")

if __name__ == "__main__":
    populate_portfolio_optimization_benchmark_dataset()
