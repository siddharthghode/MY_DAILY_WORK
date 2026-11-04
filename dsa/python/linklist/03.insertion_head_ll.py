class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
head.next=b
b.next=c
c.next=d

def delete_head(head):
    temp=head
    head=head.next
    print("now head is=",head.data)
    return head
        
head=delete_head(head)
current=head
while current is not None:
    print(current.data)
    current=current.next
        
    