# Exceptions

# try:
#      $ some lines of code $
#
# except <Error1>:
#      $ handler <Error1>
#
# except <Error2>:
#      $ handler <Error2>
#
# else:
#      $ no exeptions were raised, the code run successfully
#
# finally:
#      $ do something in any case

from logging import exception
from msilib.schema import Error


try:
    result = 2 / 0
except ZeroDivisionError:
    print('Can not divide by zero')
finally:
    result = 10

print(result)  # 10

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Raise own exception

try:
    raise Exception('An Error')
except Exception as error:
    print(error)

# Create own exception using class


class DogNotFoundExceptions(Exception):
    pass


try:
    raise DogNotFoundExceptions()
except DogNotFoundExceptions as error:
    print(error)
