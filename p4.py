import networkx as nx

MISSING = object()
def my_clustering(graph, vert = MISSING):

    if vert == MISSING:
        return overall_clustering(graph)
        

    #get vertex degree
    degree = graph.degree(vert)

    #bail if degree is 0
    if degree == 0:
        return 0

    #get all neighbors
    neighbors = g.neighbors(vert)
    
    num_con_neighbors = 0.0

    #loops through neighbors and their neighbors
    for n in neighbors:
        for consec in neighbors:
            if n == consec:
                continue

            #if neighbors are connected increment number of connected neighbors
            if consec in g.neighbors(n):
                num_con_neighbors += 1
    
    #bail if num neighbors connections is 0
    if num_con_neighbors == 0:
        return 0

    num_con_neighbors /= 2

    #return clustering coefficient
    return (2*(num_con_neighbors))/ (degree * (degree - 1))

def overall_clustering(graph):
    clustering = {}

    #call my_clustering and create dictionary of clustering
    for v in graph.nodes():
        clustering[v] = my_clustering(graph, v)

    return clustering

g = nx.Graph({0:[3,6], 1:[3,5], 2:[4,7], 3:[0,1,6], 4:[2], 5:[1], 6:[0,3], 7:[2]})

print nx.clustering(g)
#print overall_clustering(g)
print my_clustering(g, 3)
print my_clustering(g)
