class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node must not be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    def position(self, key):
        pos = 0
        current = self.head

        while current:
            if current.data == key:
                return pos
            current = current.next
            pos += 1

        return -1

    def delete_node(self, key):
        dummy = Node(0)
        dummy.next = self.head

        prev = dummy
        current = self.head

        while current:
            if current.data == key:
                prev.next = current.next
                break
            prev = current
            current = current.next

        self.head = dummy.next


# ---------------- TEST ----------------
llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_beginning(40)
llist.insert_at_end(20)
llist.insert_at_end(30)

llist.delete_node(20)
llist.print_list()     # 40 --> 10 --> 30 --> None

llist.delete_node(999) # not found (ignored)
llist.print_list()     # 40 --> 10 --> 30 --> None