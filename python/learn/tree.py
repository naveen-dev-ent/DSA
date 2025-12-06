#Breadth First Search (level order)

from collection import deque

def level_order(root):
	if root is None:
		print("Empty Node")

	queue = [deque(root)]

	while queue:
		node = queue.popleft()
		print(node.data, end=" ")
		if node.left:
			queue.append(current.left)
		if node.right:
			queue.append(current.right)

def inorder(node):
	if node:
		inorder(node.left)
		print(node.data, end="")
		inorder(node.right)

def preorder(node):
	if node:
		print(node.data, end=" ")
		preorder(node.left)
		preorder(node.right)

def postorder(node):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.data, end=" ")
	


