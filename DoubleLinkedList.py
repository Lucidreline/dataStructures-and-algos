class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Adding to list
    def push(self, value):  # adds to end of list
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value, self.tail)
            self.tail = self.tail.next

        self.size += 1

    def unshift(self, value):  # adds to head of list
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.head.prev = Node(value, None, self.head)
            self.head = self.head.prev

        self.size += 1

    def insert(self, value, index):  # inserts node at an index
        if self.size < 1 or index is self.size:
            self.push(value)

        elif index is 0:
            self.unshift(value)

        else:
            target = self.fetchIndex(index)
            newNode = Node(value, target.prev, target)
            target.prev.next = newNode
            target.prev = newNode

        self.size += 1

    # remove from list

    # get from list

    def fetchIndex(self, index):
        if self.size < 1:
            raise Exception("Can't fetch from empty list")

        elif index < 0:
            raise Exception(
                "This Double Linkedlist does not support negative integers.")

        elif self.size < index:
            raise Exception("Can't fetch index " + str(index) +
                            " when list only goes up to index " + str(self.size))

        elif index < self.size/2:  # walk through list from head
            target = self.head
            for i in range(index):
                target = target.next

            return target

        else:  # walk through list backwards
            target = self.tail
            for i in range((self.size - index) - 1):
                target = target.next

            return target

    def fetchValue(self, value):
        if self.size < 1:
            return None

        else:
            target = self.head
            for i in range(self.size):
                if target.value is value:
                    return target
                target = target.next

            return None

    def get(self, index):
        return self.fetchIndex(index).value

    def contains(self, value):
        if self.fetchValue(value):
            return True
        else:
            return False

    # change from list

    # display
    def printDetailed(self):
        target = self.head
        while target:
            lefty = ""
            righty = ""
            if target.prev:
                lefty = str(target.prev.value)
            else:
                lefty = "*"

            if target.next:
                righty = str(target.next.value)
            else:
                righty = "*"

            print(lefty + "<- " + str(target.value) + " -> " + righty)
            target = target.next
