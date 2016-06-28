
def reverse(str):
    """Returns the reverse of a string in place

    >>> reverse("apple")
    'elppa'

    >>> reverse("cat")
    'tac'
    """

    new_str = ""
    for i in range(len(str), 0, -1):
    	new_str += str[i-1]
    return new_str

def count_list(lst):
    """Counts a list recursively

    >>> count_list([3, 6, 8, 2])
    4

    >>> count_list([])
    0
    """
    if not lst:
        return 0
    return 1 + count_list(lst[1:])

def print_recursively(lst):
    """Prints a list recursively

    >>> print_recursively([1, 2, 3])
    1
    2
    3
    
    >>> print_recursively([])
    0
    """
    if not lst:
        return 0
    
    print lst[0]
    print_recursively(lst[1:])

# def recursive_index(needle, haystack):
#     """Find the index of an item in a list using recursion.

#     >>> recursive_index("hey", ["hey", "there", "you"])
#     0

#     >>> recursive_index("cat", ["hey", "there", "you"])
#     None
#     """
    ## FIX ME 

def no_duplicates(str_):
    """Determine if a string has all unique characters
    >>> no_duplicates("unique")
    False
    """
    for char in str_:
        if str_.count(char) > 1:
            return False
    return True

def binary_search(val):
    """Using binary search, return the num of guesses it will take to guess the val given

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2
    """
    assert 0 < val < 101
    
    num_guesses = 0
    min_guess = 0
    max_guess = 101
    guess = None


    while guess != val:
        num_guesses += 1
        guess = (max_guess - min_guess) / 2 + min_guess

        if guess > val:
            max_guess = guess
        elif guess < val:
            min_guess = guess

    return num_guesses

def missing_num(lst, val):
    """Finds the missing number in a list

    >>> missing_num([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    >>> missing_num([0, 1, 3], 3)
    2
    """

    lst.sort()
    min_val = lst[0]
    for i in range(min_val, (val+1)):
        if i not in lst:
            return i

def polish_calc(s):
    """Implements a polish calculator

    >>> polish_calc("+ 1 2")
    3

    >>> polish_calc("/ 6 - 4 2")
    3
    """
    # convert to a list
    lst = s.split()
    # pop the last number -- 2
    num1 = int(lst.pop())

    while lst:
        # pop the last number (again) -- 4
        num2 = int(lst.pop())
        # pop the last operand -- -
        op1 = lst.pop()
        # perform calculation depending on last operand
        if op1 == "+":
            op2 = num2 + num1
        elif op1 == "-":
            op2 = num2 - num1
        elif op1 == "/":
            op2 = num2 / num1
        elif op1 == "*":
            op2 = num2 * num1

    return op2

def is_prime(val):
    """Returns whether or not a value is prime
    >>> is_prime(13)
    True

    >>> is_prime(5)
    True

    >>> is_prime(6)
    False
    """

    is_prime = True
    for i in range(2, val):
        if val % i == 0:
            is_prime = False
    return is_prime

def primes(num):
    """Returns a list of the number of prime numbers of given value
    >>> primes(1)
    [2]

    >>> primes(4)
    [2, 3, 5, 7]
    """
    primes = []
    i = 2
    while len(primes) < num:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def print_backwards(num):
    """Returns the number, reversed
    >>> print_backwards(413)
    314

    >>> print_backwards(249)
    942
    """
    num_str = str(num)
    reverse = num_str[::-1]
    reverse_int = int(reverse)
    return reverse_int


class Node(object):
    """Implementing a node class"""
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next

class LinkedList(object):
    """Implementing a linked list class"""

    def __init__(self, head, tail):
        self.head = None
        self.tail = None
    # methods - print list, finding a node by its data, adding a node, removing a node
    def print_list(self):
        """Print all items in the list"""
        # set current to head
        current = self.head
        while current is not None:
            print current.data
            current = current.next

    def find_node(self, data):
        """Find a node with the given data"""
        current = self.head
        while current is not None:
            if current.data == data:
                return True

            current = current.next

    def add_node(self, data):
        """Add a node to the linked list"""
        # first, instantiate a new node
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def remove_node(self, value):
        # if there is a head and the head is the value we want
        if self.head and self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return

            else:
                current = current.next

def print_recursively_backwards(lst):
    """Print list backwards

    >>> print_recursively_backwards(["cat", 4, True])
    True
    4
    cat
    """
    if not lst:
        return
    print_recursively_backwards(lst[1:])
    print lst[0]

def miss_num(lst, max_num):
    """Return missing num from list

    >>> miss_num([5, 3, 6, 2, 4], 6)
    1
    >>> miss_num([1, 2, 3, 4, 5], 6)
    6
    """

    i = 1
    lst = sorted(lst)
    for num in lst:
        if num != i:
        # if not num == i:
            return i
        i = i+1
    return max_num

# def return_index(lst, item):
#     """
#     >>> return_index(["hey", "there", "you"], "you")
#     2
#     >>> return_index(["hey", "there", "you"], "cat")
#     None
#     """
#     if not lst:
#         return None
#     count = 0
#     if lst[0] == item:
#         return count
#     count += return_index(lst[1:],item)+1
#     return count

## Sorting 
def sequentialSort(alist, item):
    """Implements sequential sort
    >>> sequentialSort([4, 3, 8, 1, 9], 2)
    False
    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

def sequentialOrderedSort(alist, item):
    """Implements sequential sort
    >>> sequentialSort([4, 3, 8, 1, 9], 2)
    False
    """
    pos = 0
    found = False
    stop = False
    alist = alist.sort()
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else: 
                pos += 1
    return found

def binarySearch(alist, item):
    """Implements binary search
    >>> binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 2)
    True
    """
    # declare the first and last item (need in order to find the midpoint)
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def reverse_ll_in_place(head):
    """Given LL head node, return head node of new, reversed linked list."""

    previous = head
    current = head.next 
    while current.next != None:
        current = current.next
        previous = current
    current = head 
    current.next = previous
    while previous.next != None:
        previous = previous.next
        current = previous
    return head

def reverse_ll(head):

    # reverse iterate through the ll 
    # create new nodes 
    new_head = None
    n = head 
    while n:
        new_head = Node(n.data, new_head)
        n = n.next
    return new_head

def show_even_indices(lst):
    """Write a function that returns the indices of all the numbers which are even
    >>> show_even_indices([1, 2, 3, 4, 6, 8])
    [1, 3, 4, 5]
    """
    evens_list = []

    if not lst:
        return None

    for index, item in enumerate(lst):
        if item % 2 == 0:
            evens_list.append(index)
    return evens_list

def sorted_lists(lst1, lst2):
    """Write a function that returns a new list that is the sorted merge of both of them. For the above lists, our result would be:
    >>> sorted_lists([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
    """
    new_list = []
    i = 0
    j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            new_list.append(lst1[i])
            i += 1
        else:
            new_list.append(lst2[j])
            j += 1
    
    new_list.extend(lst1[i:])
    new_list.extend(lst2[j:])

    return new_list

# def split(string, splitter):
#     """Write a function that splits a string on a given word.
#     >>> split("that is which is that which is that", " that ")
#     ['that is which is', 'which is that']
#     """
#     string_lst = list(string)
#     splitter_lst = list(splitter)
#     i = 0
#     j = 0

#     new_lst = []

#     if splitter not in string:
#         return list(string)

#     while i < len(string_lst) and j < len(splitter_lst):
#         if string_lst[i] != splitter_lst[j]:
#             new_list.append(string_lst[i])

# def longest_palindrome(str):
#     """Returns the longest palindrome in a string
#     >>> longest_palindrome("abcdefghba")
#     1
#     >>> longest_palindrome("baablkj12345432133d")
#     9
#     """
#     longest_pal = 0
#     # for a char, iterate through until we find that char again
#     # if not found, continue
#     # if found, pass that substring into _is_pal
#     # if true, compare the length of that substring with longest pal
#     i = 0
#     j = 0

#     while i < range(len(str)) and j < range(len(str)):
#         if str[i] != str[j]:
#             i = i+1
#             j = j+1
#             continue
#         else:
#             # returns a True / False
#             answer = _is_pal(str[i:j])
#             if answer == True and answer > len(longest_pal):
#                 longest_pal = str[i:j]
#     return longest_pal
    
def _is_pal(s):
    is_pal = True
    for i in range(len(s)/2):
        if s[i] == s[-i-1]:
            is_pal = True
        else:
            is_pal = False

