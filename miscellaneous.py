"""Miscellaneous functions using Graph Data Structure."""
from validate import *
from properties import *

def TSortUtility(obj,vertex,visited,stack):
    """Utility function for Topological Sorting."""
    for nbrVertex in obj.adjList[vertex]:
        if visited[nbrVertex]:
            continue
        visited[nbrVertex] = True
        TSortUtility(obj,nbrVertex,visited,stack)
    stack.append(vertex)    

def TSort(obj):
    """Topological Sorting."""
    validateTSort(obj)      #Validate the pre-requisite of topological sort
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


def MSTKruskal(obj):
    """Returns a minimum spanning tree using Kruskal's Algorithm with Union by Rank heuristic."""
    #The graph must be connected and undirected
    validateConnected(obj)
    validateUndirected(obj)

    def find(parent,vertex):
        """Utility function FIND for union by rank heuristics."""
        if parent[vertex]==vertex:
            return vertex
        return find(parent,parent[vertex])

    def union(parent, rank, x, y):
        """Utility function UNION for union by rank heuristics.""" 
        xroot = find(parent, x) 
        yroot = find(parent, y)
        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        else:
            parent[yroot] = xroot

    def Cycle(edge,parent):
        """Cycle detection in the Graph."""
        if find(parent,edge[0])==find(parent,edge[1]):
            return True
        if parent[edge[1]]==edge[1]:
            parent[edge[1]] = edge[1]
        else:
            parent[edge[0]] = edge[1]
        return False

    #Making a list containing all the edges of graph in the form (v1,v2,weight)
    graphList = []
    for vertex in obj.adjList:
        for index,nbrVertex in enumerate(obj.adjList[vertex]):
            if (vertex,nbrVertex,obj.weightList[vertex][index]) not in graphList and (nbrVertex,vertex,obj.weightList[vertex][index]) not in graphList:
                graphList.append((vertex,nbrVertex,obj.weightList[vertex][index]))

    graphList = sorted(graphList,key=lambda item: item[2])  #sorting graph wrt the weight
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

def Dijkstra(obj,source):
    """Determination of minimum distance between vertex using Dijkstra Algorithm.
    Returns the distance  as well as the parent of each vertex to trace the path"""
    validatePositiveWeight(obj)     #All the edge weights must be positive.

    def minDistVertex(minDist,sptSet):
        """Return minimum distance between vertices."""
        minD = float("inf")

        for vertex in minDist:
            if not sptSet[vertex] and minDist[vertex]<=minD:
                minVertex = vertex
                minD = minDist[vertex]
        return minVertex

    sptSet = dict()     #Spanning set containing all the visited covered 
    minDist = dict()    
    parent = dict() 
    for vertex in obj.vertexList:
        sptSet[vertex] = False
        minDist[vertex] = float("inf")
        parent[vertex] = vertex
    minDist[source] = 0

    SPT = []  #Shortest Path Tree (node,parent,weight)

    for i in range(CountVertices(obj)):
        vertex = minDistVertex(minDist,sptSet)
        sptSet[vertex] = True
        for index,nbrVertex in enumerate(obj.adjList[vertex]):
            if minDist[vertex]+obj.weightList[vertex][index]<minDist[nbrVertex]:
                minDist[nbrVertex] = minDist[vertex]+obj.weightList[vertex][index]
                parent[nbrVertex] = vertex
    return minDist,parent


def bellmanFord(obj,source):
    """Determination of minimum distance between vertices using Bellman Ford Algorithm."""
    validatePositiveWeight(obj)
    n = CountVertices(obj)
    minDist = dict()
    for vertex in obj.vertexList:
        if vertex == source:
            minDist[vertex] = 0
        else:
            minDist[vertex] = float("inf")

    #Comparing if minDist[i]+edge_weight(i,j)<minDist[j]
    for i in range(n-1):
        for vertex in obj.adjList:
            for nbrVertex in obj.adjList[vertex]:
                if minDist[nbrVertex]>minDist[vertex]+obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)]:
                    minDist[nbrVertex] = minDist[vertex]+obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)]
    return minDist


def minDistance(obj,source=None,dest=None):
    """Generic function for determination of minimum distance between
    vertices for increasing rubustness and user-friendliness."""
    if validatePositiveWeight(obj,exception=False):     #If dijkstra can be used.
        if source!=None:
            minD,_ = Dijkstra(obj,source)	#Also returns the parent to trace the path
            if dest!=None:
                return minD[dest]
            return minD
        
    n = CountVertices(obj)
    minDist = dict()
    for vertex in obj.vertexList:
        minDist[vertex] = dict()

    for vertex in obj.vertexList:
        for nbrVertex in obj.vertexList:
            if vertex == nbrVertex:
                minDist[vertex][nbrVertex] = 0
            else:
                try:
                    minDist[vertex][nbrVertex] = obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)]
                except:
                    minDist[vertex][nbrVertex] = float("inf")
    
    for intermediate in obj.vertexList:
        for source in obj.vertexList:
            for dest in obj.vertexList:
                if minDist[source][intermediate]+minDist[intermediate][dest]<minDist[source][dest]:
                    minDist[source][dest] = minDist[source][intermediate]+minDist[intermediate][dest]
    
    if source!=None:
        if dest!=None:
            return minDist[source][dest]
        return minDist[source]
    return minDist
