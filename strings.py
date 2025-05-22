
text = "Hello, World!"

# Basic Operations
print("Length:", len(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# Concatenation
name = "Alice"
greeting = "Hello, " + name
print("Greeting:", greeting)

# Slicing Strings
text2 = "Programming"
print("First 6 characters:", text2[0:6])
print("Last character:", text2[-1])
print("Reversed string:", text2[::-1])

# Splitting and Joining
sentence = "I love Python programming"
words = sentence.split(" ")
print("Split into words:", words)
hyphenated = "-".join(words)
print("Hyphenated string:", hyphenated)

# String Formatting
name = "John"
age = 25
print(f"My name is {name} and I'm {age} years old.")
print("My name is {} and I'm {} years old.".format(name, age))

# Checking Substrings
text3 = "Data Science"
print("Contains 'Data':", "Data" in text3)
print("Starts with 'Da':", text3.startswith("Da"))
print("Ends with 'ce':", text3.endswith("ce"))