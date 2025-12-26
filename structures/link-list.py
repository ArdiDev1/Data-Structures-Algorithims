class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return  # Key not found
        if prev is None:
            self.head = current.next  # Remove head
        else:
            prev.next = current.next  # Bypass the node to be removed


ll = LinkedList()

# Example usage:ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
ll.remove(2)
ll.display()  # Output: 1 -> 3 -> None
ll.reverse()
ll.display()  # Output: 3 -> 1 -> None
ll.append(4)
ll.display()  # Output: 3 -> 1 -> 4 -> None
