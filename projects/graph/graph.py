"""
STEPS

    - MAKE A FUNCTION IN GRAPH CLASS FOR.. 
    - add_vertex / node
    - add_edge   / connection
    - get_neighbors
    
    - bfs ( BREADTH-FIRST SEARCH )
    - bft ( breadth-first traversal )
    
    - dft ( depth-first traversal )
    - dft_recursive ( ^ but recursive )
    - dfs ( DEPTH-FIRST SEARCH)
    - dfs_recursive ( ^ but revcursive )
"""
from util import Stack, Queue  # These may come in handy


# ------------------------------------------------- INITIAL GRAPH CLASS (WITH HELPER FUNCTIONS)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
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


    # ------------------------------------------------- BREADTH-FIRST TRAVERSAL

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        
        q.enqueue(starting_vertex)
        
        while q.size() > 0:
            # Dequeue a vert
            current_node = q.dequeue()
            # If not visited
            if current_node not in visited:
                print(current_node)
                # Mark as visited
                visited.add(current_node)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_node):
                    q.enqueue(neighbor)
    
    
    
    # ------------------------------------------------- BREADTH-FIRST SEARCH
    
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue() # create a queue
        visited = set() # create an empty "visited" set {}
        
        q.enqueue([starting_vertex]) # add starting inx to the queue
        
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            
            if current_node not in visited: # nothing initially
                visited.add(current_node)   # add that to the visited {}
                if current_node is destination_vertex:
                    return path
                else:
                    neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                # build path for each of 1's neighbors
                new_path = path.copy()
                new_path.append(neighbor)
                q.enqueue(new_path)
                


    # ------------------------------------------------- DEPTH-FIRST TRAVERSAL
    
    
    def dft(self, starting_vertex): 
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        
        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                for next_vertex in self.get_neighbors(current_node):
                    s.push(next_vertex)

                    
    
    
    # ------------------------------------------------- DEPTH-FIRST TRAVERSAL (RECURSIVELY)

    def dft_recursive(self, starting_vertex_id, visited=None):

        if visited is None:
            visited = set()

        visited.add(starting_vertex_id)

        print(starting_vertex_id) # prints first recursively

        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                
    # ------------------------------------------------- DEPTH-FIRST SEARCH
    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        lst = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                visited.add(current_node)
                lst.append(current_node)
                if current_node == destination_vertex:
                    return lst

                for next_vertex in self.get_neighbors(current_node):
                    s.push(next_vertex)
                    
                    
                    
    # ------------------------------------------------- DEPTH-FIRST SEARCH (RECURSIVELY)

    def dfs_recursive(self, starting_vert, ending_vert, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vert)

        path = path + [starting_vert]  # subtly makes a copy of the path

        """
        # Line above equivalent to:

        path = list(path)  # make a copy
        path.append(starting_vert)
        """

        if starting_vert == ending_vert:
            return path

        for neighbor in self.get_neighbors(starting_vert):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, ending_vert, visited, path)
                if new_path is not None:
                    return new_path

        return None






if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(f"GRAPH.VERTICES => {graph.vertices}")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(f" BFT RESULT => {graph.bft(1)}")
    print(f" NEIGHBORS => {graph.get_neighbors(2)}")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(f"DFT Result => {graph.dft(1)}")
    print(f"DFT RECURSIVE RESULT -> {graph.dft_recursive(1)}")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f"BFS Result => {graph.bfs(1, 6)}")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f"DFS RESULT -> {graph.dfs(1, 6)}")
    print(f"DFS RECURSIVE RESULT -> {graph.dfs_recursive(1, 6)}")
