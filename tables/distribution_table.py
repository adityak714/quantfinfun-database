from sqlalchemy import Column, DateTime, ARRAY, String, Float
from sqlalchemy.dialects.postgresql import UUID
from tables import get_attributes, Base


class DistributionDataset(Base):
    __tablename__ = "distribution_table"
    
    unique_id = Column(UUID, primary_key=True)
    date = Column(DateTime)
    assets = Column(ARRAY(String))
    distribution = Column(ARRAY(Float))
    
    def __repr__(self) -> None:
        return get_attributes(self)
    
    def __str__(self) -> None:
        return get_attributes(self)