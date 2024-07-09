class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def addVertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def addEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
            except ValueError:
                pass
            return True
        return False
    
    def removeEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)

            del self.adj_list[vertex]
            return True
        return False

graph = Graph()

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")

graph.addEdge("A", "B")
graph.addEdge("B", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "D")
graph.addEdge("C", "D")

#graph.removeEdge("A", "B")
graph.removeVertex('D')
graph.printGraph()