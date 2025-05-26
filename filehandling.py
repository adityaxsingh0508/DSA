# File Handling: Write, Append, and Read

# 1. Write to the file (creates or overwrites)
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")

# 2. Append to the same file
with open('example.txt', 'a') as file:
    file.write("This line is appended.\n")

# 3. Read from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:\n")
    print(content)