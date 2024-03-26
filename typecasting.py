#typecasting = The process of converting a value of one data type to another
#              (string, integer, float, boolean)
#              Explicit vs Implicit

name = ""
age = 21
gpa = 1.9
student = True

## EXPLICIT
# FLOAT
age = float(age)
print(age)

# INT
gpa = int(gpa)
print(gpa)

# STRING
student = str(student)
print(student)

# BOOLEAN
age = bool(age)
print(age)

name = bool(name)
print(name)

## IMPLICIT
# TYPE
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

x = 2
y = 2.0
x = x / y
print(x)
