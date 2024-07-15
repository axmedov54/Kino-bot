import sqlite3

def fetch_data():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
