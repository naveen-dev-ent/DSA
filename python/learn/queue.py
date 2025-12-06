class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		self.length = 0

	def enqueue(self, element):
		new_node = Node(element)
		if self.front is None:
			self.front = self.rear = new_node
		else:
			self.rear.next = new_node
			self.rear = new_node
		self.length += 1

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty")
		else:
			temp = self.front.data
			self.front = self.front.next
			if self.front is None:
				self.rear = None
			self.length -= 1 
			return temp

	def peek(self):
		if self.is_empty():
			print("Queue is empty")
		else:
			return self.front.data

	def is_empty(self):
		return self.length == 0

	def size(self):
		return self.length

myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
print(myQueue.peek())  # 'A'
print(myQueue.dequeue())  # 'A'
print(myQueue.size())  # 1


		 
		
			