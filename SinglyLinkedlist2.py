from symtable import Class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node


    def insertAtTheEnd(self,new_data):
        new_node = Node(new_data)
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
        if self.head.next is None:
            self.head =None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deleteFromBeginnning(self):
        if self.head is None:
            return "The linked list is Empty"
        self.head = self.head.next

    def printLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

if __name__ == ("__main__"):
    llist = LinkedList()
    llist.insertAtTheBeginning('fox')
    llist.insertAtTheBeginning('brown')
    llist.insertAtTheBeginning('quick')
    llist.insertAtTheBeginning('A')
    llist.printLinkedList()

    llist.insertAtTheEnd("jumped")
    llist.insertAtTheEnd("in")
    llist.insertAtTheEnd("the")
    llist.insertAtTheEnd("river")
    llist.printLinkedList()

    llist.deleteFromBeginnning()
    llist.printLinkedList()

    llist.deleteFromEnd()
    llist.printLinkedList()
