import time
import sqlite3 
import functools


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


#### paste your with_db_decorator here

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    print(f"[LOG] Attempt {attempt} of {retries}")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[LOG] ERROR occurred: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            # If all retries fail, raise the last exception
            print("[LOG] All retries failed.")
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)