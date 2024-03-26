# variable = a resuable container for storing a value
#            a variable behaves as if it were the value it contains

# VARIABLES
age = 21
print(age)
print("You are " + str(age) + " years old")
print("You are", age, "years old")
print(f"You are {age} years old")

# INTEGER
age = 21
players = 2
quantity = 5
print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT
gpa = 3.2
distance = 2.5
price = 10.99
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")
print(f"The price is ${price}")

# STRING
name = "Bro"
food = "pizza"
email = "Bro123@gmail.com"
print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# BOOLEAN
online = True
for_sale = False
running = True
print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")

# EXAMPLE 1
x, y, z = 1, 2, 3
x = y = z = 1
print(x)
print(y)
print(z)





