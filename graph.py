import numbers
from validate import *
from traversal import *
from miscellaneous import *
from properties import *

class Graph:

    def addVertex(self,ver):
        self.vertex.add(ver)

    def addEdge(self,i,j,weight=0):
        validateEdge(i,j,weight,self.vertexList,"Check the Edge List")
        try:
            if j not in self.adjList[i]:
                self.adjList[i].append(j)
                self.weightList[i].append(weight)
            else:
                self.weightList[i][self.adjList[i].index(j)] = weight
        except KeyError:
            self.adjList[i] = list([j])
            self.weightList[i] = list([0])
            
    def unDirectional(self):
        unGraph = uniGraph(self.vertexList,self.adjList,self.weightList)
        return unGraph
        #self.vertexList = unGraph.vertexList
        #self.adjList = unGraph.adjList
        #self.weightList = unGraph.weightList
        #del unGraph

    def reverse(self):
        newAdjList = dict()
        newWeightList = dict()
        for vertex in self.adjList:
            newWeightList[vertex] = []
        for vertex in self.vertexList:
            newAdjList[vertex] = []

        for vertex in self.adjList:
            for (index,nbrVertex) in enumerate(self.adjList[vertex]):
                newAdjList[nbrVertex].append(vertex)
                newWeightList[nbrVertex].append(self.weightList[vertex][index])
        self.adjList = newAdjList
        self.weightList = newWeightList
        del newAdjList
        del newWeightList
        
        

    def __init__(self,vertexList=set(),adjList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
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
                raise Exception("Vertex list and Weight List contains different number of elements")

        self.weightList = dict()
        for vertex in adjList.keys():
            self.weightList[vertex] = [0 for conVertex in adjList[vertex]]
        for vertex in weightList.keys():
            for (index,weight) in enumerate(weightList[vertex]):
                self.weightList[vertex][index] = weight
            

class uniGraph(Graph):
    def __init__(self,vertexList=set(),adjList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
        self.adjList = dict()
        self.weightList = dict()
        self.edgeCount = 0
        self.vertexCount = len(self.vertexList)
        
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
                self.addEdge(nbrVertex,vertex,0)
                self.edgeCount += 1
                try:
                    assert weightList[vertex][adjList[vertex].index(nbrVertex)]==weightList[nbrVertex][adjList[nbrVertex].index(vertex)]
                except AssertionError:
                    raise Exception("Ambiguous Weight List")
                except:
                    pass    
        for vertex in self.vertexList:
            if vertex not in self.adjList.keys():
                self.adjList[vertex]=[]



        try:
            for vertex,nbrWeightList in weightList.items():
                if len(nbrWeightList)> len(adjList[vertex]):
                    raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))
        except:
            raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))        
        for vertex,neighborhood in adjList.items():
            for nbrVertex in neighborhood:
                ind_vertex = self.adjList[nbrVertex].index(vertex)
                ind_nbrVertex = self.adjList[vertex].index(nbrVertex)
                try:
                    self.weightList[vertex][ind_nbrVertex] =  weightList[vertex][adjList[vertex].index(nbrVertex)]
                    self.weightList[nbrVertex][ind_vertex] =  weightList[vertex][adjList[vertex].index(nbrVertex)]
                except:
                    pass
                
                
#x = Graph([1,2,3,5,4,4],{1:[2,3],2:[3,5],3:[4,5],4:[3,5]},{1:[5,1],2:[5,1]})
#print(CountRegions(x))
#x = Graph([0,1,2,3,4,5],{2:[1],3:[1],4:[2,0],5:[3]})
#print(x.adjList,x.weightList)
#x.reverse()
#print(x.adjList,x.weightList) 
#print(DFS(x,2))
#print(TSort(x))
#validateWeaklyConnected(x)
#print("Components:",len(Components(x.unDirectional())))
