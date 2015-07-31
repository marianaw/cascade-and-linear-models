from linear_threshold import linear_threshold
from independent_cascade import independent_cascade
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from seed_algorithms import greedy_ICM, greedy_LTM, high_degree, distance_centrality, random_choice
from igraph import Graph


k = 5
x = [i for i in range(0, k)]


def ltmodel (g, iterations, k, st):
    gr = []
    hd = []
    ce = []
    ra = []

    for i in range(0, k):
        seed = greedy_LTM(g, iterations, i, st)
        S, _, _ = linear_threshold(g, seed, 0)
        gr.append(len(S))

    for i in range(0, k):
        seed = high_degree(g, i)
        S, _, _ = linear_threshold(g, seed, 0)
        hd.append(len(S))

    for i in range(0, k):
        seed = distance_centrality(g, i)
        S, _, _ = linear_threshold(g, seed, 0)
        ce.append(len(S))

    for i in range(0, k):
        seed = random_choice(g, i)
        S, _, _ = linear_threshold(g, seed, 0)
        ra.append(len(S))

    plt.plot(x, gr, color='r')
    plt.plot(x, hd, color='g')
    plt.plot(x, ce, color='k')
    plt.plot(x, ra, color='b')
    plt.ylabel('Active nodes set size.')
    plt.xlabel('Target set size.')
    red_patch = mpatches.Patch(color='red', label='Greedy.')
    green_patch = mpatches.Patch(color='green', label='High degree.')
    bl_patch = mpatches.Patch(color='black', label='Distance centrality.')
    blue_patch = mpatches.Patch(color='blue', label='Random.')
    plt.legend(handles=[red_patch, green_patch, bl_patch, blue_patch])
    plt.show()
    plt.show()



def icmodel_1 (g, iterations, k, st):
    p = 0.1
    gr = []
    hd = []
    ce = []
    ra = []
    for i in range(0, k):
        seed = greedy_ICM(g, iterations, p, i, st, 1)
        S, _ , _ = independent_cascade(g, seed, p, 0, 1)
        gr.append(len(S))
    for i in range(0, k):
        seed = high_degree(g, i)
        S, _ , _ = independent_cascade(g, seed, p, 0, 1)
        hd.append(len(S))
    for i in range(0, k):
        seed = distance_centrality(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 1)
        ce.append(len(S))
    for i in range(0, k):
        seed = random_choice(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 1)
        ra.append(len(S))
    plt.plot(x, gr, color='r')
    plt.plot(x, hd, color='g')
    plt.plot(x, ce, color='k')
    plt.plot(x, ra, color='b')
    plt.ylabel('Active nodes set size.')
    plt.xlabel('Target set size.')
    red_patch = mpatches.Patch(color='red', label='Greedy.')
    green_patch = mpatches.Patch(color='green', label='High degree.')
    bl_patch = mpatches.Patch(color='black', label='Distance centrality.')
    blue_patch = mpatches.Patch(color='blue', label='Random.')
    plt.legend(handles=[red_patch, green_patch, bl_patch, blue_patch])
    plt.show()



def icmodel_2 (g, iterations, k, st):
    p = 0.01
    gr = []
    hd = []
    ce = []
    ra = []
    for i in range(0, k):
        seed = greedy_ICM(g, iterations, p, i, st, 1)
        S, _ , _ = independent_cascade(g, seed, p, 0, 1)
        gr.append(len(S))
    for i in range(0, k):
        seed = high_degree(g, i)
        S, _ , _ = independent_cascade(g, seed, p, 0, 1)
        hd.append(len(S))
    for i in range(0, k):
        seed = distance_centrality(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 1)
        ce.append(len(S))
    for i in range(0, k):
        seed = random_choice(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 1)
        ra.append(len(S))
    plt.plot(x, gr, color='r')
    plt.plot(x, hd, color='g')
    plt.plot(x, ce, color='k')
    plt.plot(x, ra, color='b')
    plt.ylabel('Active nodes set size.')
    plt.xlabel('Target set size.')
    red_patch = mpatches.Patch(color='red', label='Greedy.')
    green_patch = mpatches.Patch(color='green', label='High degree.')
    bl_patch = mpatches.Patch(color='black', label='Distance centrality.')
    blue_patch = mpatches.Patch(color='blue', label='Random.')
    plt.legend(handles=[red_patch, green_patch, bl_patch, blue_patch])
    plt.show()



def wcmodel (g, iterations, k, st):
    p = 0.1
    gr = []
    hd = []
    ce = []
    ra = []
    for i in range(0, k):
        seed = greedy_ICM(g, iterations, p, i, st, 2)
        S, _ , _ = independent_cascade(g, seed, p, 0, 2)
        gr.append(len(S))
    for i in range(0, k):
        seed = high_degree(g, i)
        S, _ , _ = independent_cascade(g, seed, p, 0, 2)
        hd.append(len(S))
    for i in range(0, k):
        seed = distance_centrality(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 2)
        ce.append(len(S))
    for i in range(0, k):
        seed = random_choice(g, i)
        S, _, _ = independent_cascade(g, seed, p, 0, 2)
        ra.append(len(S))
    plt.plot(x, gr, color='r')
    plt.plot(x, hd, color='g')
    plt.plot(x, ce, color='k')
    plt.plot(x, ra, color='b')
    plt.ylabel('Active nodes set size.')
    plt.xlabel('Target set size.')
    red_patch = mpatches.Patch(color='red', label='Greedy.')
    green_patch = mpatches.Patch(color='green', label='High degree.')
    bl_patch = mpatches.Patch(color='black', label='Distance centrality.')
    blue_patch = mpatches.Patch(color='blue', label='Random.')
    plt.legend(handles=[red_patch, green_patch, bl_patch, blue_patch])
    plt.show()
    
    
    
if __name__ == '__main__':
    filename = 'g.txt'
    g = Graph.Read_Edgelist(open(filename, 'r'))
    iterations = 3
    st = 2
    #ltmodel (g, iterations, k, st)
    icmodel_1(g, iterations, k, st)
    #icmodel_2(g, iterations, k, st)
    #wcmodel (g, iterations, k, st)
    
     