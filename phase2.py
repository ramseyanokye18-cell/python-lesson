'''
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
number_3 = int(input("Enter a number: "))
print(max(number_1,number_2,number_3))

if number_1>= number_2 and number_1>= number_3:
    print(f"The largest number is {number_1}")
elif number_2>=number_1 and number_2>=number_3:
    print(f"The largest number is {number_2}")
else:
    print(f"The largest number is {number_3}")

def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average
print(calculate_average(10, 20, 30))

# PRACTICE PROBLEMS
for number in range(1,51):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  
'''
import random  
target = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
guess = int(input("Guess a number between 1 and 100: "))
attempts = attempts + 1
while guess != target:
    if guess > target:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess again: "))
    attempts = attempts + 1
print(
    f"Congratulations! You've guessed the number {target} in {attempts} attempts.")              


    