import sqlite3

# try:
#     sqliteConnection = sqlite3.connect('movies.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")

#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")


# try:
#     sqliteConnection = sqlite3.connect('movies.db')
#     sqlite_create_table_query = '''CREATE TABLE movies (
#                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                 name TEXT NOT NULL,
#                                 
#                                 video_url TEXT NOT NULL,
#                                 channel TEXT NOT NULL);'''

#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")

#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection is closed")
