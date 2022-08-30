from item import Item

# Create class instance
item = Item('Iphone', 950)

# Calling Instance Method
item.calculate_total_price()

# Збільшуємо вартість товару на 20%
item.apply_increment(0.2)

# Calculate discaunt
item.apply_discount()

# Getting an Attribute
print(item.price)

# Setting an Atributes
item.name = 'OnePlus'

# Class Method
Item.instantiante_from_csv('items.csv')
print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# CSV - Comma Separated Values

# Item.__dict__  # All the attributes for Class level
# item.__dict__  # All the attributes for instace level

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# When to use class methods and when to use static methods?


class ItemStaticClass:
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to
        instantiate objects, like I have done with CSV/JSON...
        '''

    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance.
        '''


# Those methods could be also called from instances
# item = ItemStaticClass()
# item.is_integer(5)
# item.instantiante_from_csv()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OBJECT
# CLASS
# INHERITANCE
# ENCAPSULATION
# ABSTRACTIONS
# POLYMORPHISM (різні сценарії, коли ми викликаємо один і той самий об'єкт)


# Abstractions - is to handle complexity by hiding unnecessary details from the user.
# methods ... Викликаючи один метод, в ньому може спрацьовувати декілька
# інших, які ми не показуємо та приховуємо від користувача: def __preparebody(..);
# def __connection(..). Це все методи для методу def send_email(..)

# POLYMORPHISM - різні сценарії, коли ми викликаємо один і той самий об'єкт)
# наприклад 1: Функція len() знає як визначати довжину різних типів ітерабельних
# колекцій.  2. '+' - як додавання number так і конкатинація str
