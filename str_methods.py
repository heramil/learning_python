# string methods = a set of built-in methods that you can use on strings. All string methods returns new values. They do not change the original string.

name = input("Enter your full name: ")
phone_number = input("Enter in your phone number: ")

# capitalize()
name = name.capitalize()

# count()
result = phone_number.count("-")

# find()
result = name.find("o")
    
# isalpha()
result = name.isalpha()

# isdigit()
result = name.isdigit()

# lower()
name = name.lower()

# replace()
result = phone_number.replace("-", "")

# rfind()
result = name.rfind("q")

# upper()
name = name.upper()

# BUILT-IN FUCTIONS
# len()
result = len(name)

print(result)

# Python string method program
# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")