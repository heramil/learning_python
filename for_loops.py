# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# range() = represents an immutable sequence of numbers and its commonly used for looping a specific number of times in for loops.
for x in range(1, 11):
    print(x)

# reversed() = return a reverse iterator
for x in reversed(range(1, 11)):
    print(x)

# continue = continues with the next cycle of the nearest enclosing loop
for x in range(1, 16):
    if x == 13:
        continue
    else:
        print(x)

# break = it terminates the neartest enclosing loop, skipping the optional else clause if the looop has one.
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# EXAMPLE 1
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# EXAMPLE 2
for x in range(1, 11, 3):
    print(x)
