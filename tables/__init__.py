"""Table definition common for all the other tables"""

__module__="tables.__init__"
__author__="Mohd Sadiq"
__version__="v0.1"

from sqlalchemy.orm import DeclarativeBase

from utils import get_attributes


class Base(DeclarativeBase):
    """Base Class for SQLAlchemy"""

    def __str__(self) -> str:
        return get_attributes(self)

    def __repr__(self) -> str:
        return get_attributes(self)
