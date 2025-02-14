class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇔ " if temp.next else "")
            temp = temp.next
        print()

    def remove_node(self, node):
        if not node:
            return
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
        node.next = None
        node.prev = None

    def find_node(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return temp
            temp = temp.next
        return None

if __name__ == "__main__":
    # Test Case 1
    list1 = DoublyLinkedList()
    list1.add(1)
    list1.add(2)
    list1.add(3)
    list1.add(4)
    list1.add(5)
    print("Original List:", end=" ")
    list1.print_list()
    node_to_remove1 = list1.find_node(3)
    list1.remove_node(node_to_remove1)
    print("List After Removing Node 3:", end=" ")
    list1.print_list()

    # Test Case 2
    list2 = DoublyLinkedList()
    list2.add(10)
    print("\nOriginal List:", end=" ")
    list2.print_list()
    node_to_remove2 = list2.find_node(10)
    list2.remove_node(node_to_remove2)
    print("List After Removing Node 10:", end=" ")
    list2.print_list()
