class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push_head(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node  # if List was empty

        self.head = new_node
        return new_node  