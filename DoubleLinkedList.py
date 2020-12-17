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
    def push(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            target = self.fetchIndex(self.size)
            target.next = newNode
            newNode.prev = target
            self.tail = newNode

        self.size += 1

    # remove from list

    # get from list
    def fetchIndex(self, index):
        if self.size < 1:
            raise Exception("Can't fetch from empty list")

        elif self.size < index - 1:
            raise Exception("Can't fetch index " + str(index) +
                            " when list only goes up to index " + str(self.size))

        else:
            target = self.head
            for i in range(index - 1):
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

    # display list
