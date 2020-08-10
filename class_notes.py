'''
CLASS_NOTES
- 08/10/2020
'''

'''
1) NODES ARE VERTICES
2) EDGES ARE CONNECTIONS
_________________________

3) DIRECTED VS UNDIRECTED GRAPHS
    ---> VS <--->

CYCLIC - (WATER CYCLE) - ANY WAY TO CYCLE
    - O <-> O

ACYCLIC - NO WAY TO CYCLE
    - binary search tree, cant return..
___________________________

DENSE GRAPHS - HIGH RATIO OF EDGES TO NODES, NODES ARE CONNECTED TO MANY OTHER NODES
    - many connections
    
SPARSE GRAPHS - NODES ARE CONNECTED TO FEW OTHER NODES
    - few connections

WEIGHTED GRAPHS - EDGS HAVE ASSOCIATED WEIGHTS
    - cost of traversing to nodes (numbered edges)
    
UNWEIGHTED GRAPHS - NO ASSOCIATED WEIGHTS
    - not numbered (or all have the same weight)
    
(Dykstra's algorithm finds the shorted/easiest way based on connection with weights.. (bike travel in san-fran))
___________________________

GRAPH REPRESENTATION
--------------------

ADJACENCY MATRIX:

    -   TO
    F
    R
    O
    M

    - SHOWS WHAT CONNECTS TO WHAT
    - IS THERE A CONNECTION BETWEEN C & E?
    
        - A B C E
        A|f T T T   
        B|f f f T
        C|f f f f
        E|f f f f
        
        - WITH (num) WEIGHTS
        
        - A B C E
        A|0 5 4 2   
        B|0 0 0 4
        C|0 0 0 0
        E|0 0 0 0
        

ADJACENCY LIST:

VERTEX - CONNECTS TO [VERTEX, VERTEX, VERTEX]
A: [B, C, E]
B: [E]


ADJACENCY LIST(with weights):

VERTEX - CONNECTS TO [VERTEX, VERTEX, VERTEX]
A: [(B,5), (C,7), (E,9)]
B: [(E,7)]

____________________

BREADTH-FIRST TRAVERSAL:

    - INIT (ADD STARTING NODE TO THE QUEUE)
    
    WHILE NODE IS NOT EMPTY:
        DEQUE A NODE
        IF VISITED, IGNORE IT
        ELSE:                                      QUEUE               DEQUEUE, ADD NEIGH. ADD B TO VISITED
            ADD ALL NODES NEIGHBORS TO THE QUEUE - [B,G] VISITED{C} -> [G, C,A,F,E] VISITED{C, B}
            MARK NODE AS VISITED
            
            
BREADTH-FIRST SEARCH:

    - whole point of visited-set-{} is to keep us out of a cycle

'''