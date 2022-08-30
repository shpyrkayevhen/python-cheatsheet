import csv


class Item:

    pay_rate = 0.8  # The pay rate after 20% discount
    all = []  # List with created instances

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {price} is not greater or equal than zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property Decorator = Read-Only Attribute
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('The name too long')
        else:
            self.__name = name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price *= self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.price + self.price * increment_value


    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiante_from_csv(cls, file: str):
        with open(file, 'r') as f:
            data = csv.DictReader(f)
            items = list(data)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero: 5.0, 10.0 ...
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.__name}, {self.__price}, {self.quantity})'
