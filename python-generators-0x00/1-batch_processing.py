#!/usr/bin/python3
import seed


def stream_users_in_batches(batch_size):
    """
    fetches rowa in batches
    """
    try:
        conn = seed.connect_db()
        conn.database = "alx_prodev"
        cursor = conn.cursor(dictionary=True)
    except:
        print("failed to connect to db")

    cursor.execute("SELECT * FROM user_data;")
    
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows


def batch_processing(batch_size):
    """
    processes each batch to filter users over the age of25
    """
    for batch in stream_users_in_batches(batch_size):
        users_over_25 = [user for user in batch if user['age'] > 50]
        yield users_over_25


if __name__ == "__main__":
    for filtered_batch in batch_processing(20):
        for user in filtered_batch:
            print(user)
