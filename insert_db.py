import sqlite3
import traceback
import sys

def insert_data(name, video_url):
    try:
        sqliteConnection = sqlite3.connect('movies.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO movies
                            (name,video_url, channel)  VALUES  ( ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query, (name, video_url, '@t.me/kino_bot_uz1'))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed") # sarguzasht

# name = input('ismi: ')
# 
# video_url = input('url: ')

# insert_data(name, video_url)