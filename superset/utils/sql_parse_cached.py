from functools import lru_cache
from superset.constants import LRU_CACHE_MAX_SIZE


@lru_cache(maxsize=LRU_CACHE_MAX_SIZE)
def format_cached(sql,*args, **kwargs):
    from sqlparse import parse
    return format(sql)


@lru_cache(maxsize=LRU_CACHE_MAX_SIZE)
def parse_cached(sql,*args, **kwargs):
    from sqlparse import parse
    return parse(sql)
