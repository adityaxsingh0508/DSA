stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop elements
print("Popped:", stack.pop())  # 30
print("Stack after pop:", stack)

# Peek (view top element)
print("Top element:", stack[-1])

# Check if stack is empty
print("Is stack empty?", len(stack) == 0)