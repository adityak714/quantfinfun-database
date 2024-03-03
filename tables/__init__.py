from sqlalchemy.orm import DeclarativeBase

from utils import get_attributes


class Base(DeclarativeBase):
    """Base Class for SQLAlchemy"""

    def __str__(self) -> str:
        return get_attributes(self)

    def __repr__(self) -> str:
        return get_attributes(self)
