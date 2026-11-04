class Node:
    def __init__(self,data):
      self.data=data
      self.next=None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
head=a
a.next=b
b.next=c
c.next=d

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return current.data
print(delete_tail)
        