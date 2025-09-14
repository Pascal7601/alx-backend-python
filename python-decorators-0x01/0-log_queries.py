import sqlite3
import functools
import logging
#### decorator to lof SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper_log_queries(*args, **kwargs):
        query = None
        if "query" in kwargs:
            query = kwargs["query"]
        else:
            query = args[0]
        if query:
            print(f"[LOG] Executing query: {query}")
        else:
            print(f"[LOG] No query provided")

        return func(*args, **kwargs)
    return wrapper_log_queries


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('airbnb.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")