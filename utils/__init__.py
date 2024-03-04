"""Utility Functions for the repository"""

__author__="Mohd Sadiq"
__module__="utils"
__version__="v0.1"

import logging
from typing import Any


def get_attributes(obj: Any) -> str:
    """
    returns the object representation in
    obj_name(attributes=attribute_value) format
    """
    frmt = "{}({})"
    class_ = obj.__class__.__name__
    attrs = sorted(
        (k, getattr(obj, k)) for k in obj.__mapper__.columns.keys()
    )
    sattrs = ", ".join("{}={!r}".format(*x) for x in attrs)  # pylint: disable=consider-using-f-string
    return frmt.format(class_, sattrs)


def build_logger(module_name: str):
    """
    Creates two loggers a console and a file logger and returns
    to the user.
    """
    log_file_formatter = logging.Formatter(
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
    file_handler = logging.FileHandler(filename=f"{module_name}_error.log")
    file_handler.setFormatter(log_file_formatter)
    error_logger.addHandler(file_handler)

    console_logger = logging.getLogger("console logger")
    console = logging.StreamHandler()
    console.setFormatter(log_file_formatter)
    console_logger.addHandler(console)

    error_logger.setLevel(level=logging.INFO)
    console_logger.setLevel(level=logging.INFO)
    return error_logger, console_logger
