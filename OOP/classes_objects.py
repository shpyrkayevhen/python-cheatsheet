# Class is a blueprint for creating objects
class Student:

    count = 0

    def __init__(self, name: str, house: str, patronus="Stag"):
        self.name = name                       # Error checking will be from setter
        self.house = house                     # Error checking will be from setter
        self.patronus = patronus
        Student.count += 1

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property  # (2)
    def name(self):
        return self._name

    @name.setter  # (1)
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property  # Getter
    def house(self):
        return self._house

    @house.setter  # Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    # objects method
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otetr":
                return "🦉"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🖊️"

    # Можемо викликати без створення екземпляру класу
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # Автоматично викликаємо клас з цими аргументами
        return cls(name, house)


# class instance
student = Student("Harry", "Gryffindor", "Jack Russell terrier")


# class method
student2 = Student.get()


print(Student.count)

# class method
# def main():
#    student = Student.get()
#    print(f"{student.name} is from {student.house}")


# if __name__ == "__main__":
#    main()


# def get_student():
#    name = input("Name: ")
#    house = input("House: ")

#    return Student(name, house)


# Properties (@property) - атрибут, який має більше захисних механізмів.
