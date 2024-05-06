import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)] #adjacency list 

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w)) #add vertex v to adjacency list of vertex u (weight is w)
        self.graph[v].append((u, w)) #add vertex u to adjacency list of vertex v (weight is w)

    def prim_algo(self):
        key = [sys.maxsize] * self.V #initalise list key with maximum possible values (lenght is as many vertices are there)
        parent = [-1] * self.V # parent vertex of each vertex is stored in this list
        mst_set = [False] * self.V # this list is to keep track of the vertices in the MST
        
        key[0] = 0 # setting key value for first vertex as 0
        
        for _ in range(self.V): # iterate all vertices 
            u = self.min_key(key, mst_set) # vertex with the minimum key value
            mst_set[u] = True # vertex u is now included in MST
            
            for v, w in self.graph[u]: # checking neighbors of u 
                if not mst_set[v] and w < key[v]: # if v aint in MST and if weight is less than key of v
                    key[v] = w 
                    parent[v] = u # u is made the parent of v
        
        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = sys.maxsize # minimum value is made infinity or max possible value
        min_index = -1 
        
        for v in range(self.V): # iterate all vertices 
            if key[v] < min_val and not mst_set[v]: # if key of v is less than minimum and v aint in MST
                min_val = key[v] 
                min_index = v 
        
        return min_index

    def print_mst(self, parent): # printing the MST
        print("Edge \tWeight")
        tot = 0
        for i in range(1, self.V): # iterate all vertices except first one
            print(parent[i], "-", i, "\t", self.get_weight(parent[i], i))
            tot = tot + self.get_weight(parent[i], i)
            
        print("Total Weight is ",tot)
    
    def get_weight(self, u, v):
        for vertex, weight in self.graph[u]:
            if vertex == v:
                return weight
        return None

# Example usage:
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.prim_algo()
