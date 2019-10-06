"""Contains functions related to the properties and attributes of the graph."""

def ComponentsUtility(obj, vertex, visited, component):
    """Utility Function for Components"""
    visited[vertex] = True
    component.append(vertex)
    for nxtVertex in obj.adjList[vertex]:
        if visited[nxtVertex]:
            continue
        ComponentsUtility(obj, nxtVertex, visited, component)

def Components(obj):
    """Returns the components of the graph."""
    visited = dict()
    ComponentList = []

    for ver in obj.vertexList:
        visited[ver] = False

    for vertex in obj.vertexList:   #Apply DFS with with all the vertex as source keeping the same dictionary 'visited'
        component = []
        if not visited[vertex]:
            ComponentsUtility(obj, vertex, visited, component)
            ComponentList.append(component)
    return ComponentList


def CountVertices(obj):
    """Count Vertices."""
    return len(obj.vertexList)


def EdgeList(obj, undirectional=True):
    """Returns a list containing all the edges present in the graph."""
    visited = dict()
    for vertex in obj.vertexList:
        visited[vertex] = False
    edges = []
    for vertex in obj.adjList:
        visited[vertex] = True
        for nbrVertex in obj.adjList[vertex]:
            if undirectional:
                if not visited[nbrVertex]:
                    edges.append((vertex, nbrVertex))
            else:
                edges.append((vertex, nbrVertex))
    return edges

def CountEdges(obj, undirectional=True):
    """Count Edges."""
    return len(EdgeList(obj, undirectional))


def CountComponents(obj):
    """Count Components."""
    return len(Components(obj))

def CountRegions(obj):
    """Count Regions."""
    return CountEdges(obj)-CountVertices(obj)+(CountComponents(obj)+1)
