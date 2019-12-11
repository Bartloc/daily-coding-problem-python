from collections import defaultdict
class Graph(): 
    
    def __init__(self):
         self.graph=defaultdict(list)
    
    def addEdge(self,vertex,edge=None):
        if  self.graph[vertex]==[None]:
            self.graph[vertex]=[edge]
        else:
            self.graph[vertex].append(edge)
    
    def __repr__(self):
        rep=''
        for vertex in self.graph:
            rep +="{}: (".format(vertex)
            for edge in self.graph[vertex]:
                rep +="{},".format(edge)
            rep +=")\n"
        return rep
            
def transpose_graph(graph):
    graph_transposed=Graph()
    for vertex in graph.graph:
        graph_transposed.addEdge(vertex)
    for vertex in graph.graph:
        for edge in graph.graph[vertex]:
            if edge:
                graph_transposed.addEdge(edge,vertex)
    return graph_transposed
        

#testing
    
gr=Graph()
gr.addEdge(1,2)
gr.addEdge(1,3)
gr.addEdge(2,3)
gr.addEdge(3,3)
gr.addEdge(4,2)
gr.addEdge(100,200)
gr.addEdge(200)

print(gr)
gr=transpose_graph(gr)
print(gr)

gr=Graph()
gr.addEdge('A','B')
gr.addEdge('B','C')
gr.addEdge('C')

print(gr)
gr=transpose_graph(gr)
print(gr)
