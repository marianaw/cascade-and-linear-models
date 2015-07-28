from igraph import Graph
from random import random


def chance_to_activate_1(source, target):
    '''
    First model approach on the paper. The probability of 
    u activating v is c_(u,v)/d_v.
    
    Parameters:
        @param source: the source of the edge.
        @param target: the target of the edge.
        
    Returns:
        The probability of source activating target.
    '''
    edges = [graph.es.select(_source=source, _target=target)]
    c = len(edges)
    p = edges[0]['prob'][0]
    return 1-(1-p)**c



def chance_to_activate_2(target):
    '''
    Second model approach. The probability of u activating v is
    given by 1/d_v. Note we don't need the initial probabilities for
    this approach.
    
    Parameters:
        @param target: the target of the edge.
        
    Returns:
        The probability of activation.
    '''
    vertex = g.vs.select(target)
    d = vertex.outdegree() + vertex.indegree()    
    return 1/d



def activation(verbosity, source, target):
    '''
    Calls for one or the other activation function depending on the user's
    input.
    
    Parameters:
        @param verbosity: 1 for the first model approach, 2 for the second one.
        @param source: the source of the edge.
        @param target: the target of the edge.
        
    Returns:
        Either first model approach probability of source activating target or 
        the second one depending on the verbosity chosen.
    '''
    if verbosity == 1:
        chance_to_activate_1(source, target)
    if verbosity == 2:
        chance_to_activate_2(target)
    else:
        raise ('Incorrect activation. Please select 1 or 2.')
    
    
    
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
            if random() <= activation(1, v, nb):
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
