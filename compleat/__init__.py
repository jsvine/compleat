from query import Query

VERSION = (0, 0, 1)
__version__ = ".".join(map(str,VERSION))

def suggest(query_string, lang="en"):
    return Query(query_string, lang)
