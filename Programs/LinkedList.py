class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("my linked list is empty")
            return

        itr = self.head
        llitr = ''
        while itr:
            llitr += str(itr.data) + '-->'
            itr = itr.next
        print(llitr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(99)
    ll.insert_at_begining(8)
    ll.print()
