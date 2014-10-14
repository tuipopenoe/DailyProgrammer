#!python2
# Tui Popenoe
# Challenge38E.py - Djikstra Algorithm

def djikstra(graph, source):
    distance_from_source = [0] * len(graph)
    for v in range(len(graph)):
        if distance_from_source[v] != source:
            distance_from_source[v] = None
            previous[v] = None
        Q.append(v)

    while Q is not None:
        u = []