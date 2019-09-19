from validate import *

def TSortUtility(obj,vertex,visited,stack):
    for nbrVertex in obj.edgeList[vertex]:
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

    for vertex in obj.edgeList:
        #print("ver:",vertex)
        if visited[vertex]:
            continue
        visited[vertex] = True
        
        for nbrVertex in obj.edgeList[vertex]:
            if visited[nbrVertex]:
                continue
            visited[nbrVertex] = True
            TSortUtility(obj,nbrVertex,visited,stack)
        stack.append(vertex)
    return stack

def ComponentsUtility(obj,vertex,visited,component):
    visited[vertex] = True
    component.append(vertex)
    for nxtVertex in obj.edgeList[vertex]:
        if visited[nxtVertex]:
            continue
        ComponentsUtility(obj,nxtVertex,visited,component)


def Components(obj):
    visited = dict()
    ComponentList = []

    for ver in obj.vertexList:
        visited[ver] = False

    for vertex in obj.vertexList:
        component = []
        if not visited[vertex]:
            ComponentsUtility(obj,vertex,visited,component)
            ComponentList.append(component)
    return ComponentList



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