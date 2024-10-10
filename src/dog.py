class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def bark(self):
        return f"{self.name} says miaow"

my_dog = Dog("Buddy", 3)