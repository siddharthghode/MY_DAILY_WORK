class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_and_print(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list: 10 -> 20 -> 30 -> None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

traverse_and_print(head)