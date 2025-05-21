# 1. Basic Function
def greet():
    print("Hello, welcome to Python!")

# 2. Function with Parameters
def greet_user(name):
    print(f"Hello, {name}!")

# 3. Function with Return Value
def add(a, b):
    return a + b

# 4. Default Parameters
def power(base, exponent=2):
    return base ** exponent

# 5. Keyword Arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

# 6. Variable Number of Arguments
def total(*numbers):
    return sum(numbers)

# 7. Lambda (Anonymous) Functions
square = lambda x: x * x

# 8. Nested Functions
def outer():
    def inner():
        print("Inside inner function")
    inner()

# 9. Function as Argument
def apply_function(f, value):
    return f(value)

def double(x):
    return x * 2

# ----------------------
# Function Calls (for testing)
# ----------------------

greet()

greet_user("Alice")

result = add(5, 3)
print("Sum:", result)

print("Power (default):", power(4))
print("Power (custom):", power(2, 3))

describe_pet(name="Buddy", animal="dog")

print("Total:", total(1, 2, 3, 4))

print("Square of 5:", square(5))

outer()

print("Apply function (double):", apply_function(double, 5))