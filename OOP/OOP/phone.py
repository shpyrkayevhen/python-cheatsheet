from .item import Item


class Phone(Item):

    # Call to super function to have access to all attributes/methods parents class
    def __init__(self,  name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal than zero!"
        # Assign to self object
        self.broken_phones = broken_phones
