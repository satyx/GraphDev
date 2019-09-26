from validate import *

def TSortUtility(obj,vertex,visited,stack):
    for nbrVertex in obj.adjList[vertex]:
        if visited[nbrVertex]:
            continue
        visited[nbrVertex] = True
        TSortUtility(obj,nbrVertex,visited,stack)
    stack.append(vertex)    


def TSort(obj):
    validateTSort(obj)
    visited = dict()
    stack = []

    for vertex in obj.vertexList:
        visited[vertex] = False

    for vertex in obj.adjList:
        #print("ver:",vertex)
        if visited[vertex]:
            continue
        visited[vertex] = True
        
        for nbrVertex in obj.adjList[vertex]:
            if visited[nbrVertex]:
                continue
            visited[nbrVertex] = True
            TSortUtility(obj,nbrVertex,visited,stack)
        stack.append(vertex)
    return stack





"""def MSTPrim(obj):"""


def MSTKruskal(obj):
    validateConnected(obj)
    validateUndirected(obj)

    def Cycle(edge,parent):               #Nested Function
        def fparent(parent,vertex):
            if parent[vertex]==-1:
                return vertex
            return fparent(parent,parent[vertex])

        if fparent(parent,edge[0])==fparent(parent,edge[1]):
            return True
        if parent[edge[1]]==-1:
            parent[edge[1]] = edge[0]
        else:
            parent[edge[0]] = edge[1]
        return False
    

    graph = []
    for vertex in obj.adjList:
        for index,nbrVertex in enumerate(obj.adjList[vertex]):
            if (vertex,nbrVertex,obj.weightList[vertex][index]) not in graph and (nbrVertex,vertex,obj.weightList[vertex][index]) not in graph:
                graph.append((vertex,nbrVertex,obj.weightList[vertex][index]))
        sorted(graph,key=lambda item: item[1])


    parent = dict()
    for edge in graph:
        parent[edge[0]] = -1
        parent[edge[1]] = -1

    MST = []
    for edge in graph:
        MST.append(edge)
        if Cycle(edge,parent):
            MST.pop()
    return MST

"""def MST(obj,algo="Prim"):
	validateConnected(obj)
    algoImplemented = ["Prim","Kruskal"]
    if algo=="Prim":
        return MSTPrim(obj)
    else if algo=="Kruskal":
        return MSTKruskal(obj)
    else:
        raise Exception("Argument algo can only take values from {}".format(algoImplemented))"""