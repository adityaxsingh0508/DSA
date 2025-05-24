# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Slicing
print(fruits[1:])  # Output: ['cherry', 'orange']

# Looping through list
for fruit in fruits:
    print(fruit)