class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Adding to linked list
    def unshift(self, value):  # adds node to head of list
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

    def push(self, value):  # adds node to tail of list
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return True

        target = self.head
        while not target.next is None:
            target = target.next

        target.next = newNode
        self.tail = newNode
        self.size += 1
        return True

    def insert(self, value, index):  # adds node to a index of list
        if index < 0:
            return False

        if index == 0:
            self.addFirst(value)
            return True

        prevNode = self.head

        try:
            for i in range(index - 1):
                prevNode = prevNode.next

            if prevNode.next is None:
                prevNode.next = Node(value)
                self.tail = prevNode.next
                self.size += 1
                return True

            prevNode.next = Node(value, prevNode.next)
            self.size += 1
            return True

        except AttributeError:
            print("You are trying to place " + str(value) + " at index " +
                  str(index) + " when size of linked list is " + str(self.size) + ".")
            return False

    # Removing from linked list
    def pop(self):  # removes the tail of list
        if self.head is None:
            return None

        if self.head.next is None:
            tailValue = self.head.value
            self.head = None
            self.tail = None
            self.size = 0

            return tailValue

        prevNode = self.head
        while prevNode.next.next:
            prevNode = prevNode.next

        tailValue = self.tail.value
        self.tail = prevNode
        prevNode.next = None
        self.size -= 1

        return tailValue

    def shift(self):  # removes head of list
        if self.head is None:
            return None

        headValue = self.head.value

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.size = 0

            return headValue

        self.head = self.head.next
        self.size -= 1
        return headValue

    def remove(self, index):  # removes a node at index x of the list
        if index is 0:
            return self.shift()

        if index is self.size - 1:
            return self.pop()

        prevNode = self.fetch(index - 1)
        removedValue = prevNode.next.value
        if prevNode.next.next:
            prevNode.next = prevNode.next.next

        else:
            prevNode.next = None
            self.tail = prevNode

        return removedValue

    # Changing

    def set(self, value, index):  # changed value of an element
        try:
            nodeToUpdate = self.fetch(index)
            nodeToUpdate.value = value
        except AttributeError:
            print()

    def reverse(self):  # reverses the nodes in the list in place (only things that change are the pointers)
        # if list is empty or only has one node
        if self.head is None:
            return

        # list has two or more
        target = self.head
        self.head = self.tail
        self.tail = target

        nextNode = target.next
        prevNode = None

        while target:
            nextNode = target.next
            target.next = prevNode
            prevNode = target
            target = nextNode

    # Getting

    def get(self, index):  # returns value of index x
        return self.fetch(index).value

    def fetch(self, index):  # returns node of index x
        if self.head is None:
            print("Can't get(" + str(index) + "). List is empty")
            return None

        if index < 0:
            print("Can't get negative index")
            return None

        try:
            target = self.head
            for i in range(index):
                target = target.next

            return target

        except AttributeError:
            print("You are trying to get index " + str(index) +
                  " when size of linked list is " + str(self.size) + ".")

    def toList(self):  # returns an list of linkedlist
        if self.head is None:
            return []

        newList = []
        target = self.head
        while target:
            newList.append(target.value)
            target = target.next

        return newList

    def print(self):
        listString = "["

        target = self.head
        while target:
            listString += str(target.value) + ", "
            target = target.next

        # removes the last ', ' from the string and closed bracket
        listString = listString[:-2] + "]"
        print(listString)
