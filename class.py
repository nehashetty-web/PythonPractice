class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price= price
    def cost(self):
        print(self.brand,"costs",self.price)
obj=laptop("dell",1000000)
obj.cost()

#classmethod
class car:
    wheels=4
    @classmethod
    def number_wheels(cls):
        print("all cars have ",cls.wheels,"wheels")
car.number_wheels()

#static method
class student:
    @staticmethod
    def greeting():
        print("Welcome back")
student.greeting()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# Object
s1 = Student("Neha", 85)

# Access using getter
print(s1.get_marks())   # 85

# Change using setter
s1.set_marks(95)
print(s1.get_marks())   # 95

# Wrong value
s1.set_marks(150)       # Invalid marks!