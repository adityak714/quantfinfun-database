from typing import Any

def get_attributes(obj: Any) -> str:
    frmt = "{}({})"
    class_ = obj.__class__.__name__
    attrs = sorted((k, getattr(obj, k)) for k in obj.__mapper__.column.keys())
    sattrs = ", ".join("{}={!r}".format(*x) for x in attrs)
    return frmt.format(class_, sattrs)
