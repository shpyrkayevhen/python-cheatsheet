# -- Path class - the foundation to work with files and directories --
from pathlib import Path


# -- Create absolute path to the directory or files --
Path(r"C:\Users\User\Desktop\ecommerce\__init__.py")


# -- Create path obj that represent the current folder --
Path(r"Python Standart Library\path.py")


# -- We can also combine two Path obj --
# -- we must be in this folder --

# Path() \ Path("ecommerce")
# Path() \ "ecommerce" \ "__init__.py"


# -- Get home directory of current user --

# print(Path.home())


path = Path(r"C:\Users\User\Desktop\ecommerce\__init__.py")


# -- Method path obj --

# path.exists() -> True
# path.is_file() -> True
# path.is_dir() -> False
# path.name -> __init__.py
# path.stem() -> __init__
# path.suffix() -> .py
# path.parent() -> ecommerce


# -- Create a new path obj based on this existing path      --
# -- but only change the name and the extension of the file --

# path = path.with_name("file.txt")
# print(path.absolute())


# -- Create a new path obj based on this existing path --
# -- but only change extension of the file --

path = path.with_suffix(".txt")
# path.name -> __init__.txt
