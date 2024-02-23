from sqlalchemy import create_engine
import os
from tables import Base
from tables.benchmark_dataset import BenchmarkDataset
from tables.training_dataset import TrainingDataset
from tables.stock_price import StockPriceDataset
from tables.distribution_table import DistributionDataset

def main():
    engine = create_engine(os.getenv('DB_URL'), echo=True)
    Base.metadata.create_all(engine)
    
    
if __name__=='__main__':
    main()