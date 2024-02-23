from typing import Any

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base Class for SQLAlchemy"""

    def __str__(self) -> str:
        return get_attributes(self)

    def __repr__(self) -> str:
        return get_attributes(self)


def get_attributes(obj: Any) -> str:
    frmt = "{}({})"
    class_ = obj.__class__.__name__
    attrs = sorted((k, getattr(obj, k)) for k in obj.__mapper__.column.keys())
    sattrs = ", ".join("{}={!r}".format(*x) for x in attrs)
    return frmt.format(class_, sattrs)
