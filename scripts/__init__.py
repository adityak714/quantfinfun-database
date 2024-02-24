from typing import Any
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os

def add_entry_to_database(object: Any):
    engine = create_engine(str(os.getenv("DB_URL")))
    
    with Session(engine) as session:
        session.add_all([object])
        session.commit()
