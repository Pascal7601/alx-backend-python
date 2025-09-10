#!/usr/bin/python3

import seed

def stream_user_ages():
    """
    Generator: yields user ages one by one.
    """
    try:
        conn = seed.connect_db()
        conn.database = "alx_prodev"
        cursor = conn.cursor(dictionary=True)
    except:
        print("Failed to connect to DB")
        return

    cursor.execute("SELECT age FROM user_data;")
    while True:
        row = cursor.fetchone()
        if not row:
            break
        yield row['age']


def compute_average_age():
    """
    Uses the generator to compute average age without loading all data.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average}")


if __name__ == "__main__":
    compute_average_age()
