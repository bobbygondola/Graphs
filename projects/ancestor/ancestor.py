
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


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    
    # ancestors is an array of sets: (u, v)
    # trace the graph and make a path until we reach a vertex that has no ancestors
    # if multiple vertices have no ancestors, return the last value of the longer path

    # create a dictionary for storing vertices
    vertices = {}

    # creating a graph of vertices and edges using the ancestors array
    for i in ancestors:
        # use the second element of each set as the key
        if i[1] not in vertices:
            # initialize each value as a set
            vertices[i[1]] = set()
        # add the first element of each set to its corresponding key (edges)
        vertices[i[1]].add(i[0])

    # a function for getting all ancestors of a vertex
    def _get_ancestors(vertex):
        if vertex in vertices.keys():
            return vertices[vertex]
        else:
            return [None]

    stack = Stack()               # create a stack to traverse vertices
    stack.push([starting_node])   # initialize stack with starting_node in a list (path)
    visited = set()           # initialize a visited set to track visited vertices
    paths = []                # a list to store all possible paths of ancestors


    while stack.size() > 0:       # while the stack is not empty
        path = stack.pop()           # pop a path from the top of the stack
        last_node_in_path = path[-1]             # get the last vertex of that path

        if last_node_in_path not in visited:
            visited.add(last_node_in_path)                     # mark the vertex as visited

            for ancestor in _get_ancestors(last_node_in_path):  # get all ancestors of the vertex
                if ancestor is not None:       # if there are ancestors:
                    p2 = path.copy()                   # create a copy of the current path
                    p2.append(ancestor)             # add an ancestor to the path
                    stack.push(p2)                      # add the path to the stack
                elif last_node_in_path == starting_node:       # else if there are no ancestors:
                    return -1                       # return -1

            paths.append(path)                    # append the path to the list of paths

    last = []                                  # initialize empty array to find longest path

    for i in paths:                            # iterate through paths to find the longest
        if len(i) > len(last):
            last = i   

    return last[-1]                            # return the last element of the longest path 