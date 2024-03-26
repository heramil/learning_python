# index method = a[i:j] selects all items with index k such that i <= k < j

email = input("Enter your email: ")
index = email.find("@")
username = email[:index]
domain = email[index + 1:]

print(f"The email is {email}")
print(f"The email username is {username}")
print(f"The domain is {domain}")