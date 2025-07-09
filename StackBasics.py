stack = []   # Create an empty list to represent the stack
stack.append(10)   # Add 10 to the top of the stack
stack.append(20)   # Add 20 to the top of the stack
stack.append(30)   # Add 30 to the top of the stack
print("Stack after pushes:", stack)  # Expected: [10, 20, 30]

# Peek at the top element (last element in list)
top_element = stack[-1]  # Access last element without removing it
print("Top element is:", top_element)  # Expected: 30

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")  # Expected here

# The second method is via custom classes. Here we implement a Stack class with all key operations.
class SimpleStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Add item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Remove an item from the top and return it
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    # PEEK: return the top item without removing it.
    def peek(self):
        if self.is_empty():
            raise Exception("STACK IS EMPTY")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top:", self.items)
        return

# Main program
if __name__ == "__main__":
    stack1 = SimpleStack()

    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    # Print the elements
    stack1.print_stack()

    # Peek top element
    print("Top element:", stack1.peek())  # Expected: 3000

    # Pop elements
    print("Popped:", stack1.pop())  # Expected: 3000
    stack1.print_stack()  # Expected: [1000, 2000]

    # Check if empty
    print("Is stack empty?", stack1.is_empty())  # Expected: False

    # Pop all to empty
    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping all?", stack1.is_empty())  # Expected: True