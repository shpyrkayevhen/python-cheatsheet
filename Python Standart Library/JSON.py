# JSON - JavaScript Object Notation
import json
from pathlib import Path

movies = [
    {'id': 1, 'title': 'Terminator', 'year': 1984},
    {'id': 2, 'title': 'Lindergarden Cop', 'year': 1990},
]


# -- Convert from PYTHON to JSON --
data = json.dumps(movies)

# -- Write data to a file --
Path('movies.json').write_text(data)


# -- Convert from JSON to PYTHON --
data = Path('movies.json').read_text()
movies = json.loads(data)

# -- We can read and get all data which we need --
for movie in movies:
    print(movie['title'])
