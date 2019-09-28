class Error(Exception):
    pass

class InvalidVertex(Error):
    def __init__(self,vertex,msg=""):
        print("Invalid vertex {}.{}".format(vertex,msg))

class InvalidWeight(Error):
    def __init__(self,msg=""):
        print("Invalid weight. {}".format(msg))
class AmbiguousWeightList(Error):
    def __init__(self,msg=""):
        print("Ambiguous Weight List. {}".format(msg))

class InvalidEdge(Error):
    def __init__(self,parameter,v1,v2,weightError=False,msg=""):
        if weightError:
            print("Weight {} of Edge ({},{}) is Invalid.{}".format(parameter,v1,v2,msg))
        else:
            print("vertex {} of Edge ({},{}) is Invalid.{}".format(parameter,v1,v2,msg))

class InvalidWeightList(Error):
    def __init__(self,vertex,msg=""):
        print("Invalid Edge list corresponding to vertex {}. {}".format(vertex,msg))

class GraphAttributeInconsistency(Error):
    def __init__(self,msg=""):
        print("Invalid Vertex List with respect to Weight List or Vice Versa. {}".format(msg))

class InvalidGraph(Error):
    def __init__(self,msg=""):
        print("Invalid Graph. {}".format(msg))

class NotCyclicGraph(Error):
    def __init__(self,msg=""):
        print("NOT a Cyclic Graph. {}".format(msg))

class CyclicGraph(Error):
    def __init__(self,msg=""):
        print("The Graph is Cyclic. {}".format(msg))

class NotDirectedGraph(Error):
    def __init__(self,msg=""):
        print("NOT a Directed Graph. {}".format(msg))

class DirectedGraph(Error):
    def __init__(self,msg=""):
        print("The Graph is NOT Undirected.{}".format(msg))

class NotConnectedGraph(Error):
    def __init__(self,msg=""):
        print("Disconnected Graph. {}".format(msg))

class NotWeaklyConnectedGraph(Error):
    def __init__(self,msg=""):
        print("NOT a Weakly Connected Graph. {}".format(msg))

class NegativeWeight(Error):
    def __init__(self,msg=""):
        print("Graph contains Negative Weight(s). {}".format(msg))
