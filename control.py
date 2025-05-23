# Example of if, elif, else
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Example of a for loop
print("\nFor loop example:")
for i in range(1, 6):
    print("Count:", i)

# Example of a while loop
print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1