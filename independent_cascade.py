from igraph import Graph
from random import random


def init_prob(g, p):
    for e in g.es:
        e.update_attributes({'prob': p})



def one_step(g, seed, old_edges):
    active_nodes = set()
    active_edges = set()
    for v in seed:
        #import ipdb; ipdb.set_trace()
        for nb in g.successors(v):
            if nb in seed or (v, nb) in old_edges or (v, nb) in active_edges:
                continue
            if random() <= g.es.select(_source=v, _target=nb)['prob'][0]:
                active_nodes.add(nb)
            active_edges.add((v, nb))
    seed = seed + list(active_nodes)
    return active_edges, active_nodes, seed
    
    
    
def independent_cascade(g, seed, p, st=10):
    #TODO: check if graph is empty.
    init_prob(g, p)
    old_edges = set()
    A = seed
    B = []
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
    graph = Graph.Read_Edgelist(open('somegraph.txt', 'r'))
    seed = [24325]
    A, B = independent_cascade(graph, seed, 0.4, 5)
    print (B)