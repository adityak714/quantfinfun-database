"""
    Common functions/scripts to be used among the scripts
    present in this module
"""
__author__ = "Mohd Sadiq"
__version__ = "v0.1"


import os
from typing import Any, List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_entry_to_database(objects: List[Any]):
    """
    This Function takes in a list of objects
    and adds them to their respective tables in
    the database
    """
    engine = create_engine(str(os.getenv("DB_URL")))

    with Session(engine) as session:
        session.add_all(objects)
        session.commit()
