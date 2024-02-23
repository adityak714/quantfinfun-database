from sqlalchemy import Column, DateTime, ARRAY, String

from tables import get_attributes, Base


class BenchmarkDataset(Base):
    __tablename__ = "benchmark_dataset"
    
    date = Column(DateTime, primary_key=True)
    assets = Column(ARRAY(String), primary_key=True)
    
    def __repr__(self) -> None:
        return get_attributes(self)
    
    def __str__(self) -> None:
        return get_attributes(self)