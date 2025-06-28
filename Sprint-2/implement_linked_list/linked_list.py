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
    
    def pop_tail(self):
        if not self.tail:
            return None

        value = self.tail.value
        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else: # Only one element exists in list
            self.head = None
            self.tail = None

        return value
    
    def remove(self, node):
        if node.previous:
            node.previous.next = node.next
        else: # if node is head
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else: # if node is tail
            self.tail = node.previous

        node.next = None
        node.previous = None