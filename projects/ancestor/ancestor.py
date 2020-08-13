
'''
FIND THE OLDEST RELATIVE (10)

       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        # Get all neighbors (edges) of a vertex.
        return self.vertices[vertex_id]
    

def earliest_ancestor(ancestors, starting_node):
    
    # 1.)
    # create a new graph class
    
    g = Graph()
    
    # add vertices / nodes to our graph
    for node in ancestors:
        # print(node)
        g.add_vertex(node[0])
        g.add_vertex(node[1])
    
    # add all edges to our graph
    for node in ancestors:
        g.add_edge(node[1], node[0])
    print(f"G.VERTICES -> {g.vertices}")
    
    # 2.)
    # for a BFS we need a Queue
    # add the starting vertex
    q = Queue()
    q.enqueue([starting_node])
    
    
    # 3.)
    # create a visited set
    visited = set()
    
    # create a [results] list that we will end up returning
    results = []
    
    # BEGIN REPL/loop
    
    # while length of Queue is greater than 0,
    while q.size() > 0:
    
        # create a variable and assign to dequeue
        path = q.dequeue()
        # print(f"PATH -> Q.DEQUEUE - {path}")
        
        # create a variable, assign for last varibale in path
        last_vertex = path[-1]
        
        # check if last vertex is not in visited
        if last_vertex not in visited:
            
            # add that one to visited
            visited.add(last_vertex)
            
        # for loop, using get_neighbors(last vertex)
        for neighbor in g.get_neighbors(last_vertex):
        
            # create a variable for a new path --copy
            new_path = list(path)
            
            # add neighbors to our new path
            new_path.append(neighbor)
            
            # enqueue the new path to the Queue
            q.enqueue(new_path)
            print(f"new path -> {new_path}")
            
            # append the last item of that new path.. to [results]
            results.append(new_path[-1])
            
        # if [results] list is empty
            # return -1
        if len(results) == 0:
            return -1
    # return last item of [result] list
    return results[-1]
    # print(f"RESULTS -> {results}")
            
            # new path.append(neighbors)
            # we queue that new 
            
            
    
    
    
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
    
    
    
    