#Creating a singly linked list
from symtable import Class

# class SinglyLinkedList:
#     def __init__(self, value, nextNode = None):
#         self.value = value
#         self.nextNode = nextNode
#
# snode1 = SinglyLinkedList('1')
# snode2 = SinglyLinkedList('2')
# snode3 = SinglyLinkedList('3')
# snode4 = SinglyLinkedList('4')
#
# snode1.nextNode = snode2
# snode2.nextNode = snode3
# snode3.nextNode = snode4
#
# currentNode = snode1
# while True:
#     print(currentNode.value, ">>>>", end=' ')
#
#     if currentNode.nextNode is None:
#         print("None")
#         break
#     currentNode = currentNode.nextNode
class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def insertAtTheEnd(self, data):
        new_node = Node(data)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


    def deleteFromEnd(self):
        if self.head is None:
            return "List is Empty"
        if self .head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deleteFromBeginning(self):
        if self.head is None:
            return "The linked list is Empty"
        self.head = self.head.next


    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data, end =" ")
            temp = temp.next

        print()

if __name__ == ("__main__") :
    llist = LinkedList()
    llist.insertAtTheBeginning("fox")
    llist.insertAtTheBeginning("brown")
    llist.insertAtTheBeginning("quick")
    llist.insertAtTheBeginning("The")
    llist.printLinkedList()

    llist.insertAtTheEnd("jumped")
    llist.insertAtTheEnd("out")
    llist.insertAtTheEnd("the")
    llist.insertAtTheEnd("river")
    llist.printLinkedList()