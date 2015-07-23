from igraph import Graph
from random import random


def init_prob(g, p):
    '''
    Initiallizes the probability of the edges.
    
    Parameters:
        @param g: the graph.
        @param p: the probability.
    '''
    for e in g.es:
        e.update_attributes({'prob': p})



def one_step(g, seed, old_edges):
    '''
    Performs one step of the algorithm.
    
    Parameters:
        @param g: the graph.
        @param seed: the seed or set of current active nodes.
        @param old_edges: the active edges.
    
    Returns:
        A list of active edges, active nodes, and the updated seed set.
    '''
    active_nodes = set()
    active_edges = set()
    for v in seed:
        for nb in g.successors(v):
            if nb in seed or (v, nb) in old_edges or (v, nb) in active_edges:
                continue
            if random() <= g.es.select(_source=v, _target=nb)['prob'][0]:
                active_nodes.add(nb)
            active_edges.add((v, nb))
    seed = seed + list(active_nodes)
    return active_edges, active_nodes, seed
    
    
    
def independent_cascade(g, seed, p, st=10):
    '''
    The main function. Computes the independent cascade model.
    
    Parameters:
        @param g: the graph.
        @param seed: the seed or initial set of active nodes.
        @param p: the probability to initialize the edges.
        @param: the number of steps.
       
    Returns:
        A set of active nodes and a list of the active nodes at each
        step.
    '''
    init_prob(g, p)
    old_edges = set()
    B = [seed]
    gvcount = len(set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()]))
    while st>0 and gvcount>len(seed):
        alen = len(seed)
        active_edges, active_nodes, seed = one_step(g, seed, old_edges)
        B = B + [seed]
        old_edges = old_edges.union(active_edges)
        if len(seed) == alen:
            break
        st = st - 1
    return seed, B



if __name__ == '__main__':
    graph = Graph.Read_Edgelist(open('somegraph1.txt', 'r'))
    seed = [24394, 42653]
    A, B = independent_cascade(graph, seed, 0.7, 15)
    for i in B:
        print (i)
