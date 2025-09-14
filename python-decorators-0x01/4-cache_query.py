import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # open a connection
        conn = sqlite3.connect("airbnb.db")
        try:
            # pass the connection to the function
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Extract query from kwargs or args
        query = kwargs.get("query") or (args[0] if args else None)

        if query in query_cache:
            print(f"[CACHE HIT] Returning cached result for: {query}")
            return query_cache[query]

        print(f"[CACHE MISS] Executing query: {query}")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")