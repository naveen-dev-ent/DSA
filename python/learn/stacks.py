class Stack:
	def __init__(self):
		self.stack = []

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		if(self.is_empty()):
			return "Stack is empty"
		self.stack.pop()

	def peek(self):
		if(self.is_empty()):
			return "Stack is empty"
		return self.stack[-1]

	def is_empty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)

myStack = Stack()
myStack.push('A')
myStack.push('B')
print(myStack.peek())  # 'B'
print(myStack.pop())   # 'B'
print(myStack.size())  # 1


	

	
		