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
        for v in g.neighbours(u):
            edges = [graph.es.select(_source=u, _target=v)]
            n = len(edges)
            vertex = g.vs.select(v)
            d = vertex.outdegree() + vertex.indegree()
            w = n/d
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



def one_step(g, v, seed):
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
    import ipdb; ipdb.set_trace()
    vertex = g.vs.select(v)[0]
    for n in active_nbs:
        neigh = g.es.select(_source=n[0], _target=n[1])[0]
        ss = ss + neigh.attributes()['weight']
    if ss >= vertex.attributes()['prob']:
        seed = seed + [v]
    return seed


    
def linear_threshold(g, seed):
    '''
    The main algorithm. Computes linear threshold model.
    
    Parameters:
        @param g: the graph.
        @param seed: the seed or initial set of active vertices.
        
    Returns:
        The final set of active vertices seed and a list of the
        sets of active vertices at each step.
    '''
    init_weights(g)
    init_node_probs(g)
    B = [seed]
    vs = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    for v in vs:
        if v not in seed:
            seed = one_step(g, v, seed)
        B = B + [seed]
    return seed, B    
            
            
            
if __name__ == '__main__':
    graph = Graph.Read_Edgelist(open('g.txt', 'r'))
    seed = [24394]
    A, B = linear_threshold(graph, seed)
    import ipdb; ipdb.set_trace()
    for i in B:
        print(i)