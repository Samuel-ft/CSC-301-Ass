# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    #the __init__ function is used to set initial variables for the class 
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        #the new node has a pointer to our old head 
        new_node.next = self.head
        #the new node becomes the head node 
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
         # these create a new node, if the list is empty the new node becomes the head, if not empty it will start from head and move node by node until you reach the last one 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete a node with given key
    def delete_node(self, key):
        temp = self.head

        # If head itself holds the key
        
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

     #what this does is that it moves through the list and stops when it finds the node's value to key
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next


        if temp is None:
            print(f"{key} not found in list.")
            return

        #this remove the node
        prev.next = temp.next
        temp = None
    

    # Display the list
    #these start from the head move node by node until temp becomes none and it print each data with arrows 
    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# testing the linked list
ll = LinkedList()

# Insert 5 values
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.insert_at_end(40)

print("Linked List after insertions:")
ll.display_list()

# Delete one value
ll.delete_node(20)

print("\nLinked List after deleting 20:")
ll.display_list()
