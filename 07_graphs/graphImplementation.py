# Graph Implementation

class Graph:

	def __init__(self):
		self.numberOfNodes = 0
		self.adjacentlist = {}

	def __str__(self):
		return str(self.__dict__)

	def addVertex(self, node):
		self.adjacentlist[node] = []
		self.numberOfNodes += 1

	def addEdge(self, node1, node2):
		self.adjacentlist[node1].append(node2)
		self.adjacentlist[node2].append(node1)

	def showConnection(self):
		for vertex, neighbors in self.adjacentlist.items():
			print(vertex, end = '-->')
			print(' '.join(neighbors))


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3','1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4','5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0','2')
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.showConnection()