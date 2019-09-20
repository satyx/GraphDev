from validate import *

def DFSUtility(obj,vertex,visited,subGraph):
    visited[vertex] = True
    subGraph.append(vertex)
    for nxtVertex in obj.adjList[vertex]:
        if visited[nxtVertex]:
            continue
        DFSUtility(obj,nxtVertex,visited,subGraph)

def DFS(obj,vertex,visited=dict()):
    validateVertex(vertex,obj.vertexList)
    #order = []
    #visited = dict()
    subGraph= []
    for ver in obj.vertexList:
        visited[ver] = False

    DFSUtility(obj,vertex,visited,subGraph)
    return subGraph
    """order.append(subGraph)

    for ver in visited.keys():
        if visited[ver]:
            continue
        subGraph=[]
        DFSUtility(obj,ver,visited,subGraph)
        order.append(subGraph)
    return order"""


def BFSUtility(obj,visited,vertex):
    stack = []
    subGraph = []
    stack.insert(0,vertex)
    visited[vertex] = True
    while(stack):
        subGraph.append(stack.pop())
        for nbrVertex in obj.adjList[subGraph[-1]]:
            if visited[nbrVertex]:
                continue
            stack.insert(0,nbrVertex)
            visited[stack[0]] = True
    return subGraph


def BFS(obj,vertex):
    validateVertex(vertex,obj.vertexList)
    order = []
    visited = dict()
    for ver in obj.vertexList:
        visited[ver] = False

    
    order.append(BFSUtility(obj,visited,vertex))
    for ver in visited.keys():
        if visited[ver]:
            continue
        order.append(BFSUtility(obj,visited,ver))
    return order



