import imp
from pathlib import Path
import sqlite3
import json

from click import command

# -- If this file does not exist this method create them for us --
# movies = json.loads(Path("movies.json").read_text())


# -- whis statement automatically conn.close()
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies;"
    # When we read data from database we will get a cursor obj
    cursor = conn.execute(command)
    # Cursor is a iterable object
    # (1)
    # for row in cursor:
    #    print(row)

    # (2)
    movies = cursor.fetchall()
    print(movies)

    # command = "INSERT INTO Movies VALUES (?, ?, ?);"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit()
