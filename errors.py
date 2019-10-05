"""Definiton of Custom Error Classes."""
class Error(Exception):
    """Base Class for other custom error classes."""
    pass

class InvalidVertex(Error):
    """When error is raised due to absence of vertex in the vertex list."""
    def __init__(self,vertex,msg=""):
        print("Invalid vertex {}.{}".format(vertex,msg))

class InvalidWeight(Error):
    """When error is raised due to type mismatch of edge weights."""
    def __init__(self,msg=""):
        print("Ambiguous Weight List. {}".format(msg))

class InvalidEdge(Error):
    """When error is raised due to validation of edge weight and vertices."""
    def __init__(self,parameter,v1,v2,weightError=False,msg=""):
        if weightError:
            print("Weight {} of Edge ({},{}) is Invalid.{}".format(parameter,v1,v2,msg))
        else:
            print("vertex {} of Edge ({},{}) is Invalid.{}".format(parameter,v1,v2,msg))

class InvalidWeightList(Error):
    """When error is raised due to mismatch of Adjacency list and Weight list."""
    def __init__(self,vertex,msg=""):
        print("Invalid Edge list corresponding to vertex {}. {}".format(vertex,msg))

class GraphAttributeInconsistency(Error):
    """When error is raised due to UNEQUAL number of elements
    corresponding to a vertex in adjacency list and weight list."""
    def __init__(self,msg=""):
        print("Invalid Vertex List with respect to Weight List or Vice Versa. {}".format(msg))

class InvalidGraph(Error):
    """when error is raised due to inconsistent or invalid graph attributes."""
    def __init__(self,msg=""):
        print("Invalid Graph. {}".format(msg))

class NotCyclicGraph(Error):
    """When error is raised due to Absence of cycle(s) in the graph."""
    def __init__(self,msg=""):
        print("NOT a Cyclic Graph. {}".format(msg))

class CyclicGraph(Error):
    """When error is raised due to presence of cycle(s) in the graph."""
    def __init__(self,msg=""):
        print("The Graph is Cyclic. {}".format(msg))

class NotDirectedGraph(Error):
    """When error is detected due to undirectional nature Graph."""
    def __init__(self,msg=""):
        print("NOT a Directed Graph. {}".format(msg))

class DirectedGraph(Error):
    """When error is detected due to directional nature Graph."""
    def __init__(self,msg=""):
        print("The Graph is NOT Undirected.{}".format(msg))

class NotConnectedGraph(Error):
    """When error is raised due to disconnectivity in Graph."""
    def __init__(self,msg=""):
        print("Disconnected Graph. {}".format(msg))

class NotWeaklyConnectedGraph(Error):
    """When error is raised due to non weakly connected nature of Graph."""
    def __init__(self,msg=""):
        print("NOT a Weakly Connected Graph. {}".format(msg))

class NegativeWeight(Error):
    """When error is raised due to presence of negative edge weights."""
    def __init__(self,msg=""):
        print("Graph contains Negative Weight(s). {}".format(msg))
