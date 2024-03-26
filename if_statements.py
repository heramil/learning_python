# if = do some code on IF some condition is True,
#      Else do something else

# EXAMPLE 1
online = True
if online:
    print("The user is online")
else:
    print("The user is offline")

# EXAMPLE 2
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("this item is NOT for sale")

# EXAMPLE 3
name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# EXAMPLE 3
response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# EXAMPLE 4
age = int(input('Enter your age: '))
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print("You haven't been born yet!")
else:
    print('You must be 18+ to sign up')