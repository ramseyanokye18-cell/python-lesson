#LESSON 1(VARIABLES AND PYTHON DATA TYPES)
'''
my_name = "Ramsey"
my_age = 20
my_city = "Half Assini"
print(my_name)
print(my_age)
print(type(my_age))

#LESSON 2 (STRINGS AND NUMBERS)
first_name = "Ramsey"
last_name = "Anokye"
full_name = first_name + ""+ last_name

print (full_name)
print(len(full_name))
print(full_name.upper())

a = 15
b = 4
print(a % b)
print(a ** b)

# LESSON 3 (INPUT AND OUTPUT)
Name = input("Please enter your name: ")
Birth_year = input("Enter the year you were born: ")
age_now = 2026 - int(Birth_year)
print(age_now)
print("Hello"+ " "+ Name +" "+ "you are" + " "+str(age_now)+" "+"years old")

# LESSON 4 (CONDITIONAL STATEMENTS)
number =int(input("please enter a number: "))
if number > 0 :
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# LESSON 5 (LOOPS)
for number in range(1,11):
    print(number)
number = int(input("Please enter a number: "))
while number != 0:
    number = int(input("Please enter a number: "))
print("Goodbye")

# LESSON 6(FUNCTION)
def calculate_area(length,width):
    return length * width
result = calculate_area(5,6)
print(f"The area is {result}")
print(calculate_area(10,4))
print(calculate_area(3,3))

# LESSON 7(LISTS, TUPLE, DICTONARIES, SETS)
favorite_food = ["Rice","Fufu","Waakye","Pizza","Loaded flies"]
print(favorite_food)
print(favorite_food[0])
print(favorite_food[4])
favorite_food.append("Water melon")
print(favorite_food)

student = {"name":"Ramsey",
        "age":19,
        "favorite_food":"pizza"}
print(student["name"])
print(student["age"])
print(student["favorite_food"])

# LESSON 8(BASIC ERROR HANDLING)
try:
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    total = number_1 / number_2
    print(total)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number")
finally:
    print("Program finished")    
'''
# PHASE 1 EXAMS
def first(number_1,number_2):
    return number_1 + number_2
def second(number_1,number_2):
    return number_1 - number_2
def third(number_1,number_2):
    return number_1 / number_2
def fourth(number_1,number_2):
    return number_1 * number_2
while True:
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    operator = input("choose an operator,(+, -, /,*): ")
     
    if operator == "quit":
        print("Goodbye!")
        break
    if operator == "+":
        print(first(number_1,number_2))
    elif operator == "-":
        print(second(number_1,number_2))
    elif operator == "/":
        if number_2 == 0:
            print("division by zero is not allowed")
        else:
            print(third(number_1,number_2))
    elif operator == "*":
        print(fourth(number_1,number_2))
    else :
        print("Invalid input")  




