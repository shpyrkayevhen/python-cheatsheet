from pathlib import Path

# -- This path obj represents directory "ecommerce" --
path = Path(r"C:\Users\User\Desktop\ecommerce")


# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()

# Return Generator Obj, everytime get new value
# for p in path.iterdir():
#    print(p)


# If we don't have many files can use list comprehension
paths = [p for p in path.iterdir()]
print(paths)


# We want to get only dir inside our path "ecommerce" directory
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# If we want to find in this path dir "ecommerce" files with extension .py
# All files: .glob(*.*)
# Extension: .glob(*.py)
py_files = [p for p in path.glob("*.py")]
print(py_files)


# Якщо ми хочемо шукати рекурсивно файли з розширенням .py
# в нашій path "ecommerce" папці та у папках які є в ній
rec_files = [p for p in path.rglob("**\*.py")]
print(rec_files)
