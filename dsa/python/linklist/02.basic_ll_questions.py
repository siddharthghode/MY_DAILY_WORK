# ==========================================
# 1. NODE CLASS CREATION
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data       # Stores node value
        self.next = None       # Stores reference to next node


# ==========================================
# 2. CREATING NODES
# ==========================================

a = Node(1)
b = Node(2)
c = Node(3)


# ==========================================
# 3. LINKING NODES
# ==========================================

a.next = b                   # First node points to second
b.next = c                   # Second node points to third
                               # Third node points to None


# ==========================================
# 4. ACCESSING NODE DATA
# ==========================================

print("a =", a.data, "b =", b.data, "c =", c.data)


# ==========================================
# 5. CHECKING OBJECT IDENTITIES
# ==========================================

print(id(a), " ", id(b), id(c.next))
# id(a)   -> Identity of node a
# id(b)   -> Identity of node b
# id(c.next) -> Identity of None


# ==========================================
# 6. LINKED LIST TRAVERSAL
# ==========================================

current = a                 # Start from first node

while current is not None:
    print(current.data)     # Print current node data
    current = current.next  # Move to next node


# ==========================================
# 7. COUNTING TOTAL NODES
# ==========================================

count = 0
current = a

while current is not None:
    count += 1               # Increment node count
    current = current.next   # Move to next node

print("Total nodes:", count)


# ==========================================
# 8. FINDING MAXIMUM ELEMENT
# ==========================================

maximum = float('-inf')
current = a

while current is not None:
    if maximum < current.data:
        maximum = current.data

    current = current.next

print("Maximum:", maximum)


# ==========================================
# 9. SEARCHING AN ELEMENT
# ==========================================

flag = False
n = 4                       # Element to search
current = a

while current is not None:
    if n == current.data:
        flag = True          # Element found
        break                # Stop searching

    current = current.next

print("Element found:", flag)


# ==========================================
# 10. FINDING MIDDLE NODE (TWO TRAVERSALS)
# ==========================================

i = 0
current = a

# First traversal: Count nodes
while current is not None:
    i += 1
    current = current.next

# Calculate middle index
i = i // 2

# Second traversal: Reach middle node
j = 0
middle = a

while j < i:
    middle = middle.next
    j += 1

print("Middle element:", middle.data)