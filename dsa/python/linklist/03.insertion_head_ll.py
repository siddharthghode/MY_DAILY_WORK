class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create
head=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

#link
head.next=b
b.next=c
c.next=d

#insert at head
# newnode=Node(0)
# newnode.next=head
# head=newnode
"""
while(head != None):
    print(head.data)
    head=head.next
"""
#insert at the end 
# newnode=Node(5) 
# temp=head
# while(temp.next != None):
#     temp = temp.next
# temp.next = newnode

# while(head!=None):
#     print(head.data)
#     head=head.next

#insert at the given position
position=3
newnode=Node(100)
temp=head
cnt=1
while(cnt<position-1):
    temp=temp.next
    cnt+=1
newnode.next=temp.next
temp.next=newnode


while(head!=None):
    print(head.data)
    head=head.next
