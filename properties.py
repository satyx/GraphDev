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

def CountVertices(obj):
    return len(obj.vertexList)

def EdgeList(obj,undirectional = True):
    visited = dict()
    for vertex in obj.vertexList:
        visited[vertex] = False
    edges = []
    for vertex in obj.edgeList:
        visited[vertex] = True
        for nbrVertex in obj.edgeList[vertex]:
            if undirectional:
                if not visited[nbrVertex]:
                    edges.append((vertex,nbrVertex))
            else:
                edges.append((vertex,nbrVertex))
    return edges

def CountEdges(obj,undirectional = True):
    return len(EdgeList(obj,undirectional))

def CountComponents(obj):
    return len(Components(obj))

def CountRegions(obj):
    return CountEdges(obj)-CountVertices(obj)+(CountComponents(obj)+1)