def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) #open set has nodes that are considered for exploration but not yet visited
        closed_set = set()  #contains nodes that are visited
        g = {}          # dictionary to store g(n)
        parents = {}
        g[start_node] = 0 # reaching the start node from itself is 0 cost
        parents[start_node] = start_node #start node would be own parent
        while len(open_set) > 0: # loop until open set is empty
            n = None    # variable n to store current node
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m) # if m is not in both sets, so its a new node, and added to open set
                        parents[m] = n  # parent of m is set to node n
                        g[m] = g[n] + weight # calculate cost of reaching new node m from the start node (cost of reaching n + weight of edge from n to m)
                    else:
                        if g[m] > g[n] + weight: #check if new path is less cos
                            g[m] = g[n] + weight #update it 
                            parents[m] = n
                            if m in closed_set: # re-exploring m from closed set, and hence moving it to open set
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                path = [] # empty list to store path 
                while parents[n] != n:  # goes back until reaches start node
                    path.append(n)  # appends nodes in the list from goal to start
                    n = parents[n]  
                path.append(start_node) # append start node since loop ends at that
                path.reverse()  # reverse it to start from beginning of the path
                print('Path found: {}'.format(path))
                return path
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }
        return H_dist[n] 
    
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
aStarAlgo('A', 'G')