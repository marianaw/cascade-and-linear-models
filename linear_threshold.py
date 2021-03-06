from igraph import Graph
from random import random


def init_weights(g):
    '''
    Initializes the weights of the edges of the graph.
    
    Parameters:
        @param g: the graph.
    '''
    vs = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    for u in vs:
        for v in g.neighbors(u):
            edges = g.es.select(_source=u, _target=v)
            n = len(edges)
            vertex = g.vs.select(v)[0]
            d = vertex.outdegree() + vertex.indegree()
            w = n/d
            #print ('weight', v, ':', w)
            #import ipdb; ipdb.set_trace()
            for e in edges:
                e.update_attributes({'weight': w})
     


def init_node_probs(g):
    '''
    Initializes the probabilities of the vertices with random
    distribution.
    
    Parameters:
        @param g: the graph.
    '''
    for v in g.vs:
        v.update_attributes({'prob': random()})
    
    

def in_neighbours(g, v):
    '''
    Computes the in neighbours for the vertex v.
    
    Parameters:
        @param g: the graph.
        @param v: the vertex id.
    
    Returns:
        A list of tuples with edges from the in neighbours.
    '''
    in_nbs = set()
    for e in g.get_edgelist():
        if e[1] == v:
            in_nbs.add(e)
    return in_nbs



def one_step(g, v, seed, visited):
    '''
    Performs one step of the algorithm.
    
    Parameters:
        @param g: the graph.
        @param v: the vertex to be (or not) activated.
        @param seed: the seed.
        
    Returns:
        The updated seed or set of active vertices.
    '''
    in_nbs = in_neighbours(g, v)
    active_nbs = [(n, v) for (n, v) in in_nbs if n in seed]
    ss = 0
    weights_active = set()
    vertex = g.vs.select(v)[0]
    for n in active_nbs:
        neigh = g.es.select(_source=n[0], _target=n[1])[0]
        ss = ss + neigh.attributes()['weight']
    if ss >= vertex.attributes()['prob']:
        seed = seed + [v]
        weights_active.add((v, ss))
    visited.add(v)
    return seed, weights_active, visited


    
def linear_threshold(g, seed, st):
    '''
    The main algorithm. Computes linear threshold model.
    
    Parameters:
        @param g: the graph.
        @param seed: the seed or initial set of active vertices.
        
    Returns:
        The final set of active vertices seed and a list of the
        sets of active vertices at each step. Also a list of visited nodes.
    '''
    init_weights(g)
    init_node_probs(g)
    B = []
    weights_active = set()
    visited = set(seed)
    vs = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    for v in vs:
        if v in visited:
            continue
        if v not in seed:
            seed, weights_active, visited = one_step(g, v, seed, visited)
        B = B + [weights_active]
        st = st-1
        if st == 0:
            break
    return seed, B, visited
            
            
