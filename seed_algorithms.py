from independent_cascade import independent_cascade
from linear_threshold import linear_threshold
from numpy.random import random, random_integers
from numpy import inf


def greedy_ICM(g, iterations, p, k, st, verb):
    '''
    Generates the initial seed set according to the greedy approach simulating with
    the independent cascade model.
    
    Parameters:
        @param g: the graph.
        @param iterations: the number of times we are sampling for each node to approximate σ(A).
        @param k: the size of the seed set. 
        
    Returns:
        The seed set with which to feed the algorithms.
    '''
    seed = []
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    T = iterations
    num_nodes = len(nodes)
    while len(seed) < k:
        avg = 0
        for n in nodes.difference(set(seed)):
            seed_copy = seed + [n]
            old_avg = avg
            ss = 0
            while iterations>0:
                S, _, visited = independent_cascade(g, seed_copy, p, st, verb)
                den = len(visited)
                ss = ss + len(S)/den
                iterations = iterations - 1
            avg = (num_nodes/T) * ss
            if avg > old_avg:
                current_node = n
            
            iterations = T
        seed = seed + [current_node]
            
    return seed



def greedy_LTM(g, iterations, k, st):
    '''
    Generates the initial seed set according to the greedy approach simulating with
    the linear threshold model.
    
    Parameters:
        @param g: the graph.
        @param iterations: the number of times we are sampling for each node to approximate σ(A).
        @param k: the size of the seed set. 
        
    Returns:
        The seed set with which to feed the algorithms.
    '''
    seed = []
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    T = iterations
    num_nodes = len(nodes)
    while len(seed) < k:
        
        avg = 0
        for n in nodes.difference(set(seed)):
            
            seed_copy = seed + [n]
            old_avg = avg
            ss = 0
            
            while iterations>0:
                
                S, _, visited = linear_threshold(g, seed_copy, st)
                den = len(visited)
                ss = ss + len(S)/den
                iterations = iterations - 1
            avg = (num_nodes/T) * ss

            if avg > old_avg:
                current_node = n
            
            iterations = T
        seed = seed + [current_node]
        
    return seed



def high_degree(g, k):
    '''
    Returns the first k nodes with highest degree.
    
    Parameters:
        @param g: the graph.
        @param k: the size of the seed.
        
    Returns:
        The seed.
    '''
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    degrees = []
    for n in nodes:
        vertex = g.vs.select(n)[0]
        d = vertex.outdegree() + vertex.indegree() 
        degrees.append((d, n))
    degrees = sorted(degrees, reverse=True)
    return [t[1] for t in degrees[0:k]]



def distance_centrality(g, k):
    '''
    Computes average distance to other nodes for each node.
    
    Parameters:
        @param g: the graph.
        @param k: the size of the seed.
    
    Returns:
        The seed set according to distance centrality criteria.
    '''
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    num_nodes = len(nodes)
    distances = []
    for n in nodes:
        avg = 0
        s = 0
        node = g.vs.select(n)
        for v in nodes.difference({n}):
            path = node.shortest_paths(v)[0][0]
            if path == inf:
                path = num_nodes
            s = s + path
        avg = s/(num_nodes - 1)     
        distances.append((avg, n))
    distances = sorted(distances)
    return [t[1] for t in distances[0:k]]



def random_choice(g, k):
    '''
    Randomly selects k nodes from the nodes of the graph.
    
    Parameters:
        @param g: the graph.
        @param k: the size of the seed set.
        
    Returns:
        The seed set.
    '''
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    nodes = list(nodes)
    seed = []
    for i in range(0,k):
        t = random_integers(0, len(nodes)-len(seed)-1)
        node = nodes[t]
        seed.append(nodes[t])
        nodes = list(set(nodes).difference({node}))
    return seed

