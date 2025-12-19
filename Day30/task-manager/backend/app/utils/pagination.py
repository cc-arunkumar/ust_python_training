"""from math import ceil
from sqlalchemy.orm import Query


def paginate(query: Query, page: int, limit: int):
    if page < 1:
        page = 1
    if limit < 1:
        limit = 10
    if limit > 100:
        limit = 100  # hard cap (important)

    total = query.count()
    total_pages = ceil(total / limit) if total else 1

    items = (
        query
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return {
        "data": items,
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages
    }
"""

from math import ceil
from sqlalchemy.orm import Query

def paginate(query: Query, page: int, limit: int):
    if page < 1:
        page = 1
    if limit < 1:
        limit = 10
    if limit > 100:
        limit = 100  # hard cap (important)
    total = query.count()
    total_pages = ceil(total / limit) if total else 1
    items = (
        query
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return {
        "data": items,
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages
    }