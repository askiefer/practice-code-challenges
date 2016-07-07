class Stack(object):
	
	def __init__(self):
		self.items = []

	def is_empty(self):
		return not self.items

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

def balanced_parenths(string):
	"""Returns whether or not a string has balanced brackets and parenthesis"""
	# takes in a string and puts all the open ones in a stack 
	# onces it hits a closing parenthesis, pop it and match 
	s = Stack()
	index = 0
	matches = True
	opens = '{[('
	closes = '}])'

	while index < len(string) and matches: 
		symbol = string[index]
		if symbol in opens:
			s.push(symbol)
		else:
			if s.is_empty():
				matches = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index+1

def matches(open, close):
	opens = '{[('
	closes = '})]'
	return opens.index(open) == closes.index(close)
