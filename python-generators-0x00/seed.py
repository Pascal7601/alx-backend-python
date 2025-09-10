#!/usr/bin/python3

import mysql.connector


def connect_db():
    """
    connects to the mysql database sever
    """
    connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pascal'
            )
    return connection


def create_database(connection):
    """
    creates the database called ALX_prodev if
    it does not exist
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")


def connect_to_prodev():
    """
    connects to the ALX_prodev database
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE ALX_prodev;")


def create_table(connection):
    """
    creates a table user_data if it does not esists with
    the required fields
    """
    cursor = connection.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_data (
                    user_id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    age DECIMAL(5) NOT NULL
                    );
                    """)


def insert_data(connection, data):
    """
    inserts data in the database if does not exist
    """
    cursor = connection.cursor()
    with open(data) as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            name, email, age = row[0], row[1], row[2]

            cursor.execute("INSERT INTO (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    connection.commit()




