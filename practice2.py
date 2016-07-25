########### coding challenge problems ############

def count_recursively(lst):
	"""Counts a list recursively"""
	if not lst:
		return 0
	return count_recursively(lst[1:]) + 1

def decoder(string):
	"""Decodes a string"""
	# iterate through the string
	# if it is a number, move that number of places and append the letter to 
	# a list, then join the list
	word = ""
	i = 0 
	while i < len(string):
		num_to_skip = int(string[i])
		i += num_to_skip + 1
		word = word + string[num_to_skip]
		i += 1
	return word

def missing_num(lst, num):
	"""Returns the missing num from a list giving the max_num
	>>> missing_num([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
	8
	"""
	# lst.append(num+1)
	lst.append(num+1)
	last = 0 
	for i in lst:
		if i != last+1:
			return last+1
		last += 0
	raise Exception("None missing!")

def missing_num_sum(lst, num):
	"""Sums up the numbers and subtracts the missing sum from the expected"""
	expected = sum(range(lst[0], num+1))
	# got = sum(range(lst[0], lst[-1]))
	return expected-sum(lst)

def prime_generator(num):
	"""Generates a list of prime numbers
	>>> prime_generator(5)
	[2, 3, 5, 7, 11]
	"""
	lst = []
	i = 2
	while len(lst) < num:
		if is_prime(i):
			lst.append(i)
		i += 1
	return lst

def is_prime(num):
	"""Is num a prime number"""
	is_prime = True 

	if num == 0 or num == 1:
		return
	if num < 0:
		raise ValueError("Num must be greater than 0")
	for i in range(2, num):
		if num % i == 0:
			is_prime = False
	return is_prime

def print_backwards(num):
	"""Given a digit, print a number backwards
	>>> print_backwards(314)
	413
	"""
	# could turn into a string and reverse and join
	str_lst = str(num).split("")
	new_str = ''
	i = 1
	while i < len(str_lst):
		new_str += str_lst[-i]
		i += 1
	return new_str

def print_rec(lst):
	"""Print items in a list recursively"""
	if not lst:
		return 
	print lst[0]
	return print_rec(lst[1:])

def print_backwards(lst):
	"""Print items in a list backwards recursively"""
	if not lst:
		return
	print_backwards(lst[1:])
	print lst[0]

def recursive_search(lst, item):
	"""Returns index of item sought"""
	# base case 
	if lst[0] == item:
		return
	count = recursive_search(lst[1:], item) + 1
	# FIX ME 

class Solution(object):
	def smallest_sums(nums1, nums2, k):
		# returns the pairs of numbers with the smallest sum
		# generate every possible pair from two lists 
		# sum up each pair
		i = 0
		j = 0
		pairs = []
		combins = len(nums1) * len(nums2)
		for i in nums1:
			while j < len(nums2):
				pairs.append()
			for j in nums2:

############# Linked List and methods ############
# add node
# remove node by reassigning data 
# remove node by having pointers 
# count nodes
# print all node data
# reverse linked list 

class LinkedList(object):
	def __init__(self, head):
		self.head = head
	def add_node(self, Node):
		n = self.head
		if not n:
			Node = self.head
		while n.next is not None:
			n = n.next
		n.next = Node

	def remove_node(self, Node):
		if not Node.data:
			raise ValueError("Node not in list!")
		Node.data = Node.next.data
		Node.next = Node.next.next

	def remove_node_pointers(self, value):
		if not self.head:
			raise ValueError("Empty list")
		if self.head.data == value:
			self.head = self.head.next
		current = self.head
		while current.next is not None:
			if current.next.data == value: 
				current.next = current.next.next
				return
			else:
				current = current.next

	def reverse_ll(self):
		"""Creates a new linked list that is the reverse of the given ll"""
		new_head = None
		n = self.head
		while n:
			new_head = Node(n.data, new_head)
			n = n.next

		return new_head

	def reverse_ll_in_place(self):
		"""Reverses a linked list in place"""
		current = self.head
		prev = None
		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		node.head = prev

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()





