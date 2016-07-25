## Data Structures Practice ###

######### Linked List ########## 

class Node(object):
    """Creates a node class for use in a linked list"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def given_node_remove(Node):
        """Remove a node in the ll, without using head or tail"""
        if not Node.next:
            raise ValueError("Cannot remove tail node")
        Node.data = Node.next.data
        Node.next = Node.next.next

class LinkedList(object):
    """Creates a linked list class"""
    def __init__(self):
        """Constructor for linked list class"""
        self.head = None
        self.tail = None

        # define an add_node, print_node, remove_node, find_node, size
    def add_node(self, data):
        """Adds a node to the end of the linked list"""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, value):
        """Removes a node from the list by reassigning the data of the following node"""
        # traverse the list until we find the node with the data equal to value

        if self.head and self.head.data == value:
            self.head = self.head.next
            return

        current = self.head 
        while current.next is not None:
            if current.data == value:
                current.next = current.next.next
                return
            else:
                current = current.next

    def print_node_data(self):
        """Prints all node data"""
        current = self.head
        while current is not None:
            print current.data
            current = current.next

    def find_node(self, value):
        """Traverses the list until it finds the node with the data given"""
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def size(self):
        """Returns the number of nodes in the linked list"""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next
        return count

###### Trees ########

class Tree(object):
    def __init__(self, root):
        self.root = root

class Node(object):
    def __init__(self, data, children = None):
        children = children or []
        self.data = data
        self.children = children

    def add_node(self, node):
        self.children.append(node)

    def depth_first_search(self, data):
        to_visit = [self]
        while to_visit:
            node = to_visit.pop()
            if node.data == data:
                return node
            
            to_visit.extend(node.children)

    def breadth_first_search(self, data):
        
        to_visit = [self]
        
        while to_visit:
            node = to_visit.pop(0)
            if node.data == data:
                return node
            to_visit.extend(node.children)

    def count_employees(self):
        """Counts the number of nodes in an organizational chart"""
        # start with head
        # breadth first search and incrementing count 
        count = 0
        for child in self.children:
            count = 1 + count + child.count_employees()

########### Binary Trees ##############

class BinaryNode(object):
    """Node for a binary tree"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_tree_balanced(self):
        """Is the tree at the node balanced?"""
        
        # define a helper function that evaluates whether or not a node has a right and left child
        def _left_right(self):


########### Node class and methods and Linked List ##########
class Node(object):

    def __init__(self, data, children = None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class LinkedList(object):

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext() 

    def addNode(self, Node):
        if not self.head:
            Node = self.head
        if self.tail:
            self.tail.next = Node
            Node = self.tail

    def removeNode(self, Node):
        if not self.head:
            return None
        n = self.head
        while n:
            if n.data == Node.data:
                n.data = Node.next

########## A doubly-linked list ##########

class Node(object):
    """Node class for a doubly linked list"""
    def __init__(self, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    """A doubly linked list (pointers to prev and next)"""
    ## FINISH

############## Stacks ###############

class Stack (object):
    """Implementing a stack class and its methods"""

    def __init__(self):
       self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def get_elements(self):
        return self.items
    def is_empty(self):
        return not self.items

############# Queues ################

class Queue(object):
    """A queue class and its methods"""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        self.items.pop()

    def is_empty(self):
        if not self.items:
            return True
    def size(self):
        return len(self.items)

############ Deques ###############

class Deque(object):
    """A deque class (can add and remove from either end)"""

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self, item):
        self.items.pop()

    def remove_rear(self, item):
        self.items.pop(0)

    def is_empty(self):
        if self.items:
            return True

    def size(self):
        return len(self.items)

############ Trees ################

class Tree(object):
    def __init__(self, root, children = None):
        self.root = root
        self.children = children

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def finds(self, sought):
        node = self

        while node:

            if node.data == sought:
                return node

            elif sought < node.data:
                node = node.left
                print node
                return node

            elif sought > node.data:
                node = node.right
                print node
                return node
        return None

############## Graphs ###############

class Graph(object):
    def __init__(self, root)

