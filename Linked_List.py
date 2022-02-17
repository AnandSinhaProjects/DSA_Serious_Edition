class Node:  # Represents a single class
    def __init__(self, data=None, next=None):
        self.data = data  # Data
        self.next = next  # pointer for next element


class ll:
    def __init__(self):
        self.head = None  # Points to the head of the linked list

    def insert_at_top(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(self, data)  # If the linked list is black we add the data value supplied
            return

        itr = self.head  # assigning the value of the head pointer
        while itr.next:  # This will run until we get itr.next = None
            itr = itr.next  # Moving the pointer to the last element

        itr.next = Node(data, None)  # As the loop ends this creates a Node after the last node

    # def insert_values(self, data_list):
    #     self.head = None
    #     for data in data_list:
    #         self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head  # assigning the value of the head pointer
        llstr = ''
        while itr:
            llstr += '-->' + str(itr.data)  # Printing by saving the values in a string
            print(itr.data)
            #  itr = itr.next  # used to move the pointer
        # print(llstr)


if __name__ == '__main__':
    ll = ll()
    ll.insert_at_top(5)
    # ll.insert_values([1, 2, 3, 4, 6, 7])
    ll.insert_at_end(12)
    ll.print()

    #  Check for the errors
