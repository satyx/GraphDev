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


    def find(parent,vertex):
        if parent[vertex]==vertex:
            return vertex
        return find(parent,parent[vertex])
    def union(parent, rank, x, y): 
        xroot = find(parent, x) 
        yroot = find(parent, y)
        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        else:
            parent[yroot] = xroot

    def Cycle(edge,parent):
        if find(parent,edge[0])==find(parent,edge[1]):
            return True
        if parent[edge[1]]==edge[1]:
            parent[edge[1]] = edge[1]
        else:
            parent[edge[0]] = edge[1]
        return False

    graphList = []
    for vertex in obj.adjList:
        for index,nbrVertex in enumerate(obj.adjList[vertex]):
            if (vertex,nbrVertex,obj.weightList[vertex][index]) not in graphList and (nbrVertex,vertex,obj.weightList[vertex][index]) not in graphList:
                graphList.append((vertex,nbrVertex,obj.weightList[vertex][index]))

    graphList = sorted(graphList,key=lambda item: item[2])
    parent = dict()
    rank = dict()
    for edge in graphList:
        parent[edge[0]] = edge[0]
        parent[edge[1]] = edge[1]
        rank[edge[0]] = 0
        rank[edge[1]] = 0

    MST = []
    graph_itr = 0
    mst_itr = 0

    while mst_itr < len(obj.vertexList) -1 :
        vertex1,vertex2,weight =  graphList[graph_itr] 
        graph_itr += 1
        pVertex1 = find(parent, vertex1) 
        pVertex2 = find(parent ,vertex2)

        if pVertex1 != pVertex2: 
            mst_itr += 1
            MST.append((vertex1,vertex2,weight))
            union(parent, rank, pVertex1, pVertex2) 
    
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