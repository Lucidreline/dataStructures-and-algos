from Node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addLast(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return True

        target = self.head
        while not target.next is None:
            target = target.next

        target.next = newNode
        self.size += 1
        return True

    def addToIndex(self, value, index):
        if index < 0:
            return False

        if index == 0:
            self.addFirst(value)
            self.size += 1
            return True

        prevNode = self.head

        try:
            for i in range(index - 1):
                prevNode = prevNode.next

            if prevNode.next is None:
                prevNode.next = Node(value)
                self.size += 1
                return True

            prevNode.next = Node(value, prevNode.next)
            self.size += 1
            return True

        except AttributeError:
            print("You are trying to place " + str(value) + " at index " +
                  str(index) + " when size of linked list is " + str(self.size) + ".")
            return False

    def addFirst(self, value):
        newNode = Node(value)

        if self.head is None:  # if there is no head
            self.head = newNode
            self.size += 1
            return True

        temp = self.head  # if there is a head
        self.head = newNode
        newNode.next = temp
        self.size += 1
        return True

    def toList(self):
        if self.head is None:
            return []

        newList = []
        target = self.head
        while target:
            newList.append(target.data)
            target = target.next

        return newList


listy = SinglyLinkedList()


listy.addToIndex(10, 1)

print(listy.toList())
