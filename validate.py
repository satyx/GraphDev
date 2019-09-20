import numbers
def validateVertex(vertex,vertexList,comment=""):
        if vertex not in vertexList:
            raise Exception("Invalid vertex {}.{}".format(vertex,comment))
def validateWeight(w,comment=""):
    if not (isinstance(w,numbers.Number)):
        raise Exception("Invalid Weight. {}".format(comment))

def validateEdge(v1,v2,w,vertexList,comment=""):
    validateVertex(v1,vertexList,comment)
    validateVertex(v2,vertexList,comment)
    validateWeight(w,comment)



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


def validateCyclic(obj):
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

def validateDirected(obj):
    for vertex in obj.adjList:
        for nbrVertex in obj.adjList[vertex]:
            if vertex in obj.adjList[nbrVertex]:
                return False
    return True             

def validateTSort(obj):
    if validateCyclic(obj):							#To detect self loop this validation has been kept prior to validateDirected
         raise Exception("The Graph is Cyclic")
    if not validateDirected(obj):
        raise Exception("The Graph is Non Directed")




from traversal import DFS
def validateConnected(obj,exception=True):
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
            if exception:
                raise Exception("Disconnected Graph")
            else:
                return False
    return True            
        
