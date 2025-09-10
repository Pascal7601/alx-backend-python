#!/usr/bin/python3
import seed


def stream_users():
    """
    uses a generator to fetch rows one by one from the user_data table
    """
    conn = seed.connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row

    cursor.close()
    conn.close()

