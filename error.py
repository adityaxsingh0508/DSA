try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print("Result is:", result)
finally:
    print("This block always runs, regardless of errors.")