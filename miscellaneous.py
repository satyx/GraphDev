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





"""def MSTPrim(obj):


def MSTKruskal():



def MST(obj,algo="Prim"):
	validateConnected(obj)
    algoImplemented = ["Prim","Kruskal"]
    if algo=="Prim":
        return MSTPrim(obj)
    else if algo=="Kruskal":
        return MSTKruskal(obj)
    else:
        raise Exception("Argument algo can only take values from {}".format(algoImplemented))"""
