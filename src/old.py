class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos): #TODO: Test Defauly arguement 
        self.value = value 
        self.color = 'white'
        self.pos = pos 
        self.edges = []

class Graph:
    def __init__(self):
       self.vertexes = [] 

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('T1', x=40, y=40)
        debug_vertex_2 = Vertex('T2', x=140, y=140)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2])

        print(debug_vertex_1.pos['x'])