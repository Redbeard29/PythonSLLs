class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        #If list is empty
        if self.head is None:
            self.head = new_node
            return

        #If list is not empty
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        
    def print_list(self):
        list_holder = []
        current_node = self.head
        while current_node:
            list_holder.append(current_node.data)
            current_node = current_node.next
        print(list_holder)

    def get_node_by_val(self, val):
        current_node = self.head

        while current_node:
            if current_node.data == val:
                return current_node
            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, pointer_val, data):

        prev_node = self.get_node_by_val(pointer_val)

        if not prev_node:
            print('previous node does not exist in this list')
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

myList = LinkedList()

myList.append("A")
myList.append("B")
myList.append("C")
myList.append("D")
myList.prepend("E")
myList.insert_after_node("E", "H")

myList.print_list()