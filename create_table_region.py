import sqlite3

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()

    sql = """
        CREATE TABLE region(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE    
        );
    """
    cursor.execute(sql)