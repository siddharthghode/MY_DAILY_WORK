class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(5)
second = Node(6)

# Linking nodes
first.next = second

print(first.data)
print(second.data)

# Check memory address
print(id(second.next))

# Access second node through first node
print(first.next.data)

print(" ")

print(id(first.next))
print(id(second))
print(first.next is second)