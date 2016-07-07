# Write a program that converts decimal numbers to binary, iteratively and recursively 

class Stack(object):
	"""Stack class for binary to decimal"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

def dec_to_bin(num):
	"""Converts decimal to binary iteratively using a stack
	>>> dec_to_bin(85)
	'1010101'
	"""
	rem_stack = Stack()
	# calculate the remainder when dividing by 2 each time
	while num > 0:
		rem = num % 2
		rem_stack.push(rem)
		num = num / 2
	bin_string = ""
	while not rem_stack.is_empty():
		bin_string += str(rem_stack.pop())
	return bin_string

def dec_to_bin_rec(num):
	"""Converts decimal to binary recursively
	>>> dec_to_bin_rec(85)
	'1010101'
	"""
	if num < 0:
		print "Number must be greater than 0"
		return 
	elif num == 0:
		# return an empty string, rather than '0', or else an extra
		# 0 is printed before the number
		return ''
	else:
		# if num == 1:
		# 	return str(num % 2)
		# else:
		return dec_to_bin_rec(num // 2) + str(num % 2)

