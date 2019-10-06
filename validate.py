"""Implementation functions for validation of various attribues of the Graph."""

import numbers
import warnings
from errors import *
from traversal import DFS

def validateVertex(vertex,vertexList,msg="",exception = True,warning=False):
    """Validation of vertex's presence in the vertex list."""
    if vertex not in vertexList:
        if warning:
            warnings.warn("Invalid vertex {}.{}".format(vertex,msg))
        elif exception:
            raise InvalidVertex(vertex,msg)
        else:
            return False
    return True

def validateWeight(w,msg="",exception = True,warning=False):
    """Validation of edge weight type."""
    if not (isinstance(w,numbers.Number)):
        if warning:
            warnings.warn("Invalid Weight. {}".format(msg))
        elif exception:
            raise InvalidWeight(msg)
        else:
            return False
        return True

def validateEdge(v1,v2,w,vertexList,msg="",exception = True,warning=False):
    """Validation of edges."""

    try:        #validating vertices
        validateVertex(v1,vertexList,msg,exception = exception, warning = warning )
    except:
        if warning:
            warnings.warn("Vertex {} of Edge ({},{}) is Invalid.{}".format(v1,v1,v2,msg))
        elif exception:
            raise InvalidEdge(v1,v1,v2,msg)
        else:
            return False
    
    try:        #validating vertex
        validateVertex(v2,vertexList,msg,exception = exception, warning = warning)
    except:
        if warning:
            warnings.warn("Vertex {} of Edge ({},{}) is Invalid.{}".format(v2,v1,v2,msg))
        elif exception:
            raise InvalidEdge(v2,v1,v2,msg)
        else:
            return False

    try:    #validating edge weight
        validateWeight(w,msg,exception = exception, warning = warning)
    except:
        if warning:
            warnings.warn("Weight {} of Edge ({},{}) is Invalid.{}".format(w,v1,v2,msg))
        elif exception:
            raise InvalidEdge(v2,v1,v2,msg)
        else:
            return False
    return True

def validateGraph(obj,msg="",exception = True,warning = False):
    """Validation of all the attributes of the Graph."""
    # No Need to Check Vertex validity separately

    try:    #validating edges
        for vertex in obj.adjList:
            for nbrVertex in obj.adjList[vertex]:
                validateEdge(vertex,nbrVertex,obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)],obj.vertexList)
    except:
        raise InvalidGraph(msg = "Edge ({},{}) is Invalid. ".format(vertex,nbrVertex)+msg)


def validateCyclic(obj,msg="",exception = True,warning=False):
    """Validation of cyclic nature of the Graph."""
    def validateCyclicUtility(obj,vertex,visited,stack):        #Utility Function. Applies DFS
        for nbrVertex in obj.adjList[vertex]:
            if stack[nbrVertex]:
                return True
            if visited[nbrVertex]:
                continue
            visited[nbrVertex] = True
            stack[nbrVertex] = True
            if validateCyclicUtility(obj,nbrVertex,visited,stack):
                return True
            stack[nbrVertex] = False
        return False


    #During DFS, if a vertex is detected twice, it is a cyclic graph
    detected = False
    stack = dict()
    visited = dict()
    for vertex in obj.vertexList:
        visited[vertex] = False
        stack[vertex] = False
    for vertex in obj.vertexList:
        if visited[vertex]:
            continue
        visited[vertex] = True
        stack[vertex] = True
        if validateCyclicUtility(obj,vertex,visited,stack):
            detected = True
            break
        stack[vertex] = False

    if not detected:    
        if warning:
            warnings.warn("NOT a Cyclic Graph. {}".format(msg))
        elif exception:
            raise NotCyclicGraph(msg)
        else:
            return False    
    return True

def validateDirected(obj,msg="",exception = True,warning=False):
    """Validation of directed nature of the Graph."""
    directed = False    #Flag

    #If edge between i,j an j,i exists, it is directed
    for vertex in obj.adjList:
        for nbrVertex in obj.adjList[vertex]:
            try:                #Incase the edge (a,b) or (b,a) but not both doesn't exist
                if vertex not in obj.adjList[nbrVertex] or obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)] != obj.weightList[nbrVertex][obj.adjList[nbrVertex].index(vertex)]:
                    directed = True
                    break
            except:
                directed = True
                break
        else:
            continue
        break

    if not directed:        
        if warning:
            warnings.warn("NOT a Directed Graph. {}".format(msg))
        elif exception:
            raise NotDirectedGraph(msg)
        else:
            return False
    return True             

def validateTSort(obj,msg="",exception = True,warning=False):
    """Validation of pre-requisites for Topological Sorting."""
    if validateCyclic(obj,exception=False):		#To detect self loop this validation has been kept prior to validateDirected
        if warning:
            warnings.warn("The Graph is Cyclic.{}".format(msg))
        elif exception:
            raise CyclicGraph(msg)
        else:
            return False
    if not validateDirected(obj,exception=False):
        if warning:
            warnings.warn("NOT a Directed Graph. {}".format(msg))
        elif exception:
            raise NotDirectedGraph(msg)
        else:
            return False
    return True

def validateConnected(obj,msg="",exception = True,warning=False):
    """Validation of connectivity of the Graph."""
    #Applying DFS on a graph and it's reversed form.
    #Even then, if some verticies are unvisited, its a unconnected

    visited1 = dict()
    visited2 = dict()
    for vertex in obj.vertexList:
        visited1[vertex] = False
        visited2[vertex] = False
    ver =   next(iter(obj.vertexList))  
    DFS(obj,ver,visited1)       #DFS
    obj.reverse()               #Reversing the graph
    DFS(obj,ver,visited2)       #DFS on reversed graph
    obj.reverse()               #Reversing it back.

    for vertex in obj.vertexList:       
        if not visited1[vertex] and not visited2[vertex]:
            if warning:
                warnings.warn("Disconnected Graph. {}".format(msg))
            elif exception:
                raise NotConnectedGraph(msg)
            else:
                return False
    return True
                
def validateWeaklyConnected(obj,msg="",exception = True,warning=False):
    """Validation of weakly connectivity of the Graph."""
    #If the undirected graph is connected then it is weakly connected.
    if not validateConnected(obj.undirected(),False):
        if warning:
            warnings.warn("NOT a Weakly Connected Graph. {}".format(msg))
        elif exception:
            raise NotWeaklyConnectedGraph(msg)
        else:
            return False
    return True
    

def validateUndirected(obj,msg="",exception = True, warning = False):
    """Validation of Undirectional nature of the Graph."""
    unDir = True        #flag
    for vertex in obj.adjList:
        for nbrVertex in obj.adjList[vertex]:
            if vertex not in obj.adjList[nbrVertex] or obj.weightList[vertex][obj.adjList[vertex].index(nbrVertex)] != obj.weightList[nbrVertex][obj.adjList[nbrVertex].index(vertex)]:
                unDir = False
                break
        if not unDir:
            break
    if not unDir:
        if warning:
            warnings.warn("The Graph is NOT undirected.{}".format(msg))
        elif exception:
            raise DirectedGraph(msg)
        else:
            return False
    return True

def validatePositiveWeight(obj,msg="",exception = True, warning = False):
    """Validation of the absence of negative edge weights."""
    detectNegative = False
    for vertex in obj.weightList:
        for weight in obj.weightList[vertex]:
            if weight<0:
                detectNegative = True
                break
        else:       #Executed when inner loop is not breaked
            continue
        break       #Executed when inner loop is breaked
    if detectNegative:    
        if warning:
            warnings.warn("Graph Contains Negative Weight(s). {}".format(msg))
        elif exception:
            raise NegativeWeight(msg)
        else:
            return False
    return True
