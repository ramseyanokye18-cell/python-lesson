#Classes and object
'''
class Car:
    def __init__(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = speed
    def accelerate(self):
        self.speed +=10
        print(f"Speed inreases! Now: {self.speed}km/h")    
    def introduce(self):
        print(f"Hi I am {self.brand}, with this type of {self.color} color and I can travel {self.speed}km/h")   
car1 = Car("BMW","Blue", 100) 
car2 = Car("Benz","White", 4000)
car1.introduce()
car2.introduce()
car1.accelerate()
car2.accelerate()  

# Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")
Person1 = Person("RAMSEY",19)
Person2 = Person("EMMANUEL",13)
Person1.introduce()
Person2.introduce()      

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")        
first_child = Teacher("EMMA",37)
second_child = Student("Grace",10)
first_child.introduce()
first_child.teach()
second_child.introduce()
second_child.study()

# File handling
with open("notes.txt", "w") as file:
    file.write("I'm busy\n")
    file.write("I have to study\n")
    file.write("I'm a student\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()

with open("notes.txt", "a") as file:
    file.write("Do you have money\n")
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()  

# Importing functions from another file
import mytools
print(mytools.square(5))
print(mytools.is_even(10))
print(mytools.is_even(7))
print(mytools.is_even(0))
'''
try:
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    result = number_1 / number_2
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("That's not a valid number.")
finally:    print("DONE!.")