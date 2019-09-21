import numbers
import warnings
def validateVertex(vertex,vertexList,comment="",exception = True,warning=False):
    if vertex not in vertexList:
        if warning:
            warnings.warn("Invalid vertex {}.{}".format(vertex,comment))
        elif exception:
            raise Exception("Invalid vertex {}.{}".format(vertex,comment))
        else:
            return False
    return True
def validateWeight(w,comment="",exception = True,warning=False):
    if not (isinstance(w,numbers.Number)):
        if warning:
            warnings.warn("Invalid Weight. {}".format(comment))
        elif exception:
            raise Exception("Invalid Weight. {}".format(comment))
        else:
            return False
        return True

def validateEdge(v1,v2,w,vertexList,comment="",exception = True,warning=False):
    validateVertex(v1,vertexList,comment,exception = exception, warning = warning )
    validateVertex(v2,vertexList,comment,exception = exception, warning = warning)
    validateWeight(w,comment,exception = exception, warning = warning)



def validateCyclicUtility(obj,vertex,visited,stack):
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


def validateCyclic(obj,exception = True,warning=False):
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
            return True
        stack[vertex] = False
    return False

def validateDirected(obj,comment="",exception = True,warning=False):
    for vertex in obj.adjList:
        for nbrVertex in obj.adjList[vertex]:
            if vertex in obj.adjList[nbrVertex]:
                if warning:
                    warnings.warn("Not Directed Graph.{}".format(comment))
                elif exception:
                    raise Exception("Not Directed Graph.{}".format(comment))
                else:
                    return False
    return True             

def validateTSort(obj,comment="",exception = True,warning=False):
    if validateCyclic(obj):							#To detect self loop this validation has been kept prior to validateDirected
        if warning:
            warnings.warn("The Graph is Cyclic.{}".format(comment))
        elif exception:
            raise Exception("The Graph is Cyclic.{}".format(comment))
    if not validateDirected(obj,exception=False):
        if warning:
            warnings.warn("The Graph is Non Directed.{}".format(comment))
        elif exception:
            raise Exception("The Graph is Non Directed.{}"..format(comment))




from traversal import DFS
def validateConnected(obj,exception = True,warning=False):
    visited1 = dict()
    visited2 = dict()
    for vertex in obj.vertexList:
        visited1[vertex] = False
        visited2[vertex] = False
    ver =   next(iter(obj.vertexList))  
    DFS(obj,ver,visited1)
    obj.reverse()
    DFS(obj,ver,visited2)
    obj.reverse()
    #print("satyx",visited1,visited2)
    for vertex in obj.vertexList:
        if not visited1[vertex] and not visited2[vertex]:
            if warning:
                warnings.warn("Disconnected Graph")
            elif exception:
                raise Exception("Disconnected Graph")
            else:
                return False
    return True
                
def validateWeaklyConnected(obj,exception = True,warning=False):
    if not validateConnected(obj.unDirectional(),False):
        if warning:
            warnings.warn("NOT a Weakly Connected Graph")
        elif exception:
            raise Exception("NOT a Weakly Connected Graph")
        else:
            return False
    return True
    
