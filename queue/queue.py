from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.size < self.max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("No more room left")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        else:
            print("The queue is empty")

