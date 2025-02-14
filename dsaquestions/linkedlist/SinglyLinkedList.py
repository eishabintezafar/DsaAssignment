class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def reverse(self):
        reversed_list = SinglyLinkedList()
        current = self.head
        while current:
            new_node = Node(current.data)
            new_node.next = reversed_list.head
            reversed_list.head = new_node
            current = current.next
        return reversed_list

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    # Test Case 1
    list1 = SinglyLinkedList()
    list1.add(10)
    list1.add(20)
    list1.add(30)
    print("Original List:", end=" ")
    list1.print_list()
    reversed_list1 = list1.reverse()
    print("Reversed List:", end=" ")
    reversed_list1.print_list()

    # Test Case 2
    list2 = SinglyLinkedList()
    list2.add(5)
    list2.add(10)
    list2.add(15)
    list2.add(20)
    print("\nOriginal List:", end=" ")
    list2.print_list()
    reversed_list2 = list2.reverse()
    print("Reversed List:", end=" ")
    reversed_list2.print_list()

    # Test Case 3 (Edge Case: empty list)
    list3 = SinglyLinkedList()
    print("\nOriginal List:", end=" ")
    list3.print_list()
    reversed_list3 = list3.reverse()
    print("Reversed List:", end=" ")
    reversed_list3.print_list()
