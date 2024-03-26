# while loop = execute some code WHILE some condition remains true

# EXAMPLE 1
num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")

# EXAMPLE 2
food = input("Enter your favorite food (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter your favorite food (q to quit): ")
print("bye")

# EXAMPLE 3
age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

# EXAMPLE 4
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")
