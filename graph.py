"""Definition of classes for Directional and Undirectional Graph."""
import numbers
from validate import *
from errors import *

class Graph:
    """Class for a generic directed graph."""
    def modifyWeight(self,i,j,weight=0):
        """Weight addition."""
        self.addEdge(i,j,weight)

    def addVertex(self,ver):
        """Vertex Addition."""
        self.vertex.add(ver)
        self.vertexCount+=1

    def addEdge(self,i,j,weight=0):
        """Edge addition."""
        validateEdge(i,j,weight,self.vertexList,"Check the Edge List")
        try:
            try:
                if j in self.adjList[i]:
                    pos  = self.adjList[i].index(j)
                    del self.adjList[i][pos]
                    del self.weightList[i][pos]
            finally:
                if len(self.weightList[i])==0 or weight>self.weightList[i][-1]:
                    self.weightList[i].append(weight)
                    self.adjList[i].append(j)
                else:
                    l=0
                    r = len(self.weightList[i])-1
                    while(l<=r):
                        mid = (l+r)//2
                        if self.weightList[i][mid] == weight:
                            break
                        elif self.weightList[i][mid]<weight:
                            r = mid - 1
                        else:
                            l = mid + 1
                    if (self.weightList[i][mid]<=weight):
                        self.weightList[i].insert(mid,weight)
                        self.adjList[i].insert(mid,j)
                    else:
                        self.weightList[i].insert(mid+1,weight)
                        self.adjList[i].insert(mid+1,j)
            
        except KeyError:
            self.adjList[i] = list([j])
            self.weightList[i] = list([0])
            
    def undirected(self):
        """Returns instance of the an undirected graph with same attributes."""
        undirectedGraph = unGraph(self.vertexList,self.adjList,self.weightList)
        return undirectedGraph

    def reverse(self):
        """Reverses the edge direction."""
        tempAdjList = self.adjList.copy()
        tempWeightList = self.weightList.copy()

        for vertex in self.vertexList:
            self.weightList[vertex] = []
        for vertex in self.vertexList:
            self.adjList[vertex] = []

        for vertex in tempAdjList:
            for (index,nbrVertex) in enumerate(tempAdjList[vertex]):
                self.addEdge(nbrVertex,vertex,tempWeightList[vertex][index])
                self.addEdge(vertex,nbrVertex,tempWeightList[vertex][index])
        del tempAdjList
        del tempWeightList
        
    def __init__(self,vertexList=set(),adjList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
        self.vertexCount = len(self.vertexList)

        for vertex, neighborhood in adjList.items():
            adjList[vertex] = list(set(neighborhood))

        for vertex in self.vertexList:
            if vertex not in adjList.keys():
                adjList[vertex]=[]
        for (vertex,neighborhood) in adjList.items():
            validateVertex(vertex,self.vertexList,"Check the Edge List")
            for nbrVertex in neighborhood:
                validateVertex(nbrVertex,self.vertexList,"Check the Edge List")
        self.adjList = adjList
        for vertex in self.vertexList:
            if vertex not in self.adjList.keys():
                self.adjList[vertex]=[]

        for (vertex, nbrWeightList) in weightList.items():
            validateVertex(vertex,self.vertexList,"Check Weight List")
            for nbrEdgeWeight in nbrWeightList:
                validateWeight(nbrEdgeWeight,"Check Weight List")
            if len(adjList[vertex])!=len(nbrWeightList):
                raise GraphAttributeInconsistency

        self.weightList = dict()
        for vertex in adjList.keys():
            self.weightList[vertex] = [0 for conVertex in adjList[vertex]]
            
        for vertex in self.adjList:
            for (index,nbrVertex) in enumerate(self.adjList[vertex]):
                try:
                    self.weightList[vertex][index] = weightList[vertex][index]
                except KeyError:    #If edge weight of (Vertex,nbrVertex) is not provided, Assign edge weight of (nbrVertex,Vertex) from #self.weightList and not from weightList
                    try:
                        self.weightList[vertex][index] = self.weightList[nbrVertex][self.adjList[nbrVertex].index(vertex)]
                    except:         #When neither edgeWeight of (nbrVertex,Vertex) nor of (Vertex,nbrVertex) is provided
                        pass        #Keep the edgeWeight of (Vertex,nbrVertex) as 0
            for loop_index in range(len(self.weightList[vertex])-1):
                swapped = False
                pos=0
                for pos in range(len(self.weightList[vertex])-1-loop_index):
                    if self.weightList[vertex][pos]>self.weightList[vertex][pos+1]:
                        self.weightList[vertex][pos],self.weightList[vertex][pos+1] = self.weightList[vertex][pos+1],self.weightList[vertex][pos] #Swap
                        self.adjList[vertex][pos],self.adjList[vertex][pos+1] = self.adjList[vertex][pos+1], self.adjList[vertex][pos]
                        swapped = True
                if not swapped:
                    break


class unGraph(Graph):
    """Class for a generic undirectional graph with 'Graph' as base class."""
    def addEdge(self,i,j,weight=0):
        """Edge addition."""
        super().addEdge(i,j,weight)
        super().addEdge(j,i,weight)

    def __init__(self,vertexList=set(),adjList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
        self.adjList = dict()
        self.weightList = dict()
        self.edgeCount = 0
        
        for (vertex,neighborhood) in adjList.items():
            validateVertex(vertex,self.vertexList)
            for nbrVertex in neighborhood:
                validateVertex(nbrVertex,self.vertexList,"Check the Edge List")
                
        for (vertex, nbrWeightList) in weightList.items():
            validateVertex(vertex,self.vertexList,"Check Weight List")
            for nbrEdgeWeight in nbrWeightList:
                validateWeight(nbrEdgeWeight,"Check Weight List")

        for vertex,neighborhood in adjList.items():
            for nbrVertex in neighborhood:
                self.addEdge(vertex,nbrVertex,0)
                self.edgeCount += 1
                try:
                    assert weightList[vertex][adjList[vertex].index(nbrVertex)]==weightList[nbrVertex][adjList[nbrVertex].index(vertex)]
                except AssertionError:
                    print("v1:",vertex,", v2:",nbrVertex)
                    print("w1:",weightList[vertex][adjList[vertex].index(nbrVertex)]," ,w2:",weightList[nbrVertex][adjList[nbrVertex].index(vertex)])
                    raise AmbiguousWeightList
                except (KeyError,ValueError):
                    #print("hi","neglecting an error")
                    pass
        
        for vertex in self.vertexList:
            if vertex not in self.adjList:
                self.adjList[vertex]=[]
                self.weightList[vertex] = []

        try:
            for vertex,nbrWeightList in weightList.items():
                if len(nbrWeightList)> len(adjList[vertex]):
                    raise InvalidWeightList(vertex)
        except:
            raise InvalidWeightList(vertex)

        for vertex,neighborhood in self.adjList.items():
            for nbrVertex in neighborhood:                
                ind_vertex = self.adjList[nbrVertex].index(vertex)
                ind_nbrVertex = self.adjList[vertex].index(nbrVertex)
                try:
                    w = weightList[vertex][adjList[vertex].index(nbrVertex)]    #Assign weight from adjList and not from self.adjList
                except:         #When weight of (vertex,nbrVertex) is NOT given but weight of (vertex,nbrVertex) is given
                    try:
                        w = weightList[nbrVertex][adjList[nbrVertex].index(vertex)]     #Assign of (nbrVertex,vertex) corresponding to adjList and not from self.adjList.
                    except:
                        w=0     #When edgeWeight of both (vertex,nbrVertex) and (vertex,nbrVertex) is NOT provided
                try:
                    self.weightList[vertex][ind_nbrVertex] =  w
                    self.weightList[nbrVertex][ind_vertex] =  w
                except:
                    #print("neglecting an error")
                    pass
        for vertex,neighborhood in self.adjList.items():
            loop_var = 0
            while(loop_var<len(self.weightList[vertex])-1):
                swapped = False
                pos = 0                
                while(pos<len(self.weightList[vertex])-1-loop_var):
                    if(self.weightList[vertex][pos]>self.weightList[vertex][pos+1]):
                        self.weightList[vertex][pos],self.weightList[vertex][pos+1] = self.weightList[vertex][pos+1],self.weightList[vertex][pos]
                        self.adjList[vertex][pos],self.adjList[vertex][pos+1] = self.adjList[vertex][pos+1],self.adjList[vertex][pos]
                        swapped = True
                    pos+=1

                if not swapped:
                    break
                loop_var += 1