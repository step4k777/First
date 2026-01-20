import sqlite3

DB_NAME = "shop_db"

def get_connection():
    return sqlite3.connect(DB_NAME)