# queues are a first in first out
# enqueue is when we add a new item
# dequeue is when we remove an item

class Queue(object):

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		return len(self.items)
