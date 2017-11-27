# A stack is a last in first out
# removal and addition occurs at the same place 

# to implement a Stack, we need a push, pop, peek, size, isEmpty
class Stack(object):

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
