import os
from typing import Any, List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_entry_to_database(objects: List[Any]):
    engine = create_engine(str(os.getenv("DB_URL")))

    with Session(engine) as session:
        session.add_all(objects)
        session.commit()
