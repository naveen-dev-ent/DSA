class Graph:
	def __init__(self):
		self.adj = {}

	def add_node(self, node):
		if node not in self.adj:
			self.adj[node] = []

	def add_edges(self, u, v):
		self.add_node(u)
		self.add_node(v)
		self.adj[u].append(v)
		self.adj[v].append(u)

	def print_graph(self);
		for node in self.adj:
			print(node, ":", self.adj[node])
#Breadth First Search

from collections import deque

def bfs(graph, start):
	visited = set()
	queue = deque([start])

	while queue:
		node = queue.popleft()

		if node not in visited:
			print(node.data, end=" ")
			visited.add(node)

			for neighbor in self.adj[node]:
				if neighbor not in visited:
					queue.append(child)

#Depth First Search

def dfs(graph, start, visited = None):
	if visited is None:
		visited = set()

	print(start, end = " ")
	visited.add(start)

	for neighbor in graph.adj[start]:
		if neighbor not in visited:
			dfs(graph, neighbor, visited)