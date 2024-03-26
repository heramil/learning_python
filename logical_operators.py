# logical operators = used on conditional statements

temp = 20
sunny = True

# and = checks two or more if True
if temp <= 0 and temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# or = checks if at least one condition is True
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# not = True if condition is False, and vice versa
if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")




