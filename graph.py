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
            if j not in self.edgeList[i]:
                self.edgeList[i].append(j)
                self.weightList[i].append(weight)
            else:
                self.weightList[i][self.edgeList[i].index(j)] = weight
        except KeyError:
            self.edgeList[i] = list([j])
            self.weightList[i] = list([0])
            
    def unDirectional(self):
        unGraph = uniGraph(self.vertexList,self.edgeList,self.weightList)
        return unGraph
        #self.vertexList = unGraph.vertexList
        #self.edgeList = unGraph.edgeList
        #self.weightList = unGraph.weightList
        #del unGraph

    def reverse(self):
    	newEdgeList = dict()
    	for vertex in self.vertexList:
    		newEdgeList[vertex] = []

    	for vertex in self.edgeList:
    		for nbrVertex in self.edgeList[vertex]:
    			newEdgeList[nbrVertex].append(vertex)
    	self.edgeList = newEdgeList
    	del newEdgeList


    def __init__(self,vertexList=set(),edgeList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
        for vertex, neighborhood in edgeList.items():
        	edgeList[vertex] = list(set(neighborhood))


        for vertex in self.vertexList:
            if vertex not in edgeList.keys():
                edgeList[vertex]=[]
        for (vertex,neighborhood) in edgeList.items():
            validateVertex(vertex,self.vertexList,"Check the Edge List")
            for nbrVertex in neighborhood:
                validateVertex(nbrVertex,self.vertexList,"Check the Edge List")
        self.edgeList = edgeList
        for vertex in self.vertexList:
            if vertex not in self.edgeList.keys():
                self.edgeList[vertex]=[]


        for (vertex, nbrWeightList) in weightList.items():
            validateVertex(vertex,self.vertexList,"Check Weight List")
            for nbrEdgeWeight in nbrWeightList:
                validateWeight(nbrEdgeWeight,"Check Weight List")
            if len(edgeList[vertex])!=len(nbrWeightList):
                raise Exception("Vertex list and Weight List contains different number of elements")

        if len(weightList)==0:
            self.weightList = dict()
            for vertex in edgeList.keys():
                self.weightList[vertex] = [0 for conVertex in edgeList[vertex]]
        else:
            self.weightList=weightList
            

class uniGraph(Graph):
    def __init__(self,vertexList=set(),edgeList=dict(),weightList=dict()):
        self.vertexList = set(vertexList)
        self.edgeList = dict()
        self.weightList = dict()
        self.edgeCount = 0
        self.vertexCount = len(self.vertexList)
        
        for (vertex,neighborhood) in edgeList.items():
            validateVertex(vertex,self.vertexList)
            for nbrVertex in neighborhood:
                validateVertex(nbrVertex,self.vertexList,"Check the Edge List")
                
        for (vertex, nbrWeightList) in weightList.items():
            validateVertex(vertex,self.vertexList,"Check Weight List")
            for nbrEdgeWeight in nbrWeightList:
                validateWeight(nbrEdgeWeight,"Check Weight List")

        for vertex,neighborhood in edgeList.items():
            for nbrVertex in neighborhood:
                self.addEdge(vertex,nbrVertex,0)
                self.addEdge(nbrVertex,vertex,0)
                self.edgeCount += 1
                try:
                    assert weightList[vertex][edgeList[vertex].index(nbrVertex)]==weightList[nbrVertex][edgeList[nbrVertex].index(vertex)]
                except AssertionError:
                    raise Exception("Ambiguous Weight List")
                except:
                    pass    
        for vertex in self.vertexList:
            if vertex not in self.edgeList.keys():
                self.edgeList[vertex]=[]



        try:
            for vertex,nbrWeightList in weightList.items():
                if len(nbrWeightList)> len(edgeList[vertex]):
                    raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))
        except:
            raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))        
        for vertex,neighborhood in edgeList.items():
            for nbrVertex in neighborhood:
                ind_vertex = self.edgeList[nbrVertex].index(vertex)
                ind_nbrVertex = self.edgeList[vertex].index(nbrVertex)
                try:
                    self.weightList[vertex][ind_nbrVertex] =  weightList[vertex][edgeList[vertex].index(nbrVertex)]
                    self.weightList[nbrVertex][ind_vertex] =  weightList[vertex][edgeList[vertex].index(nbrVertex)]
                except:
                    pass
                
                
#x = Graph([1,2,3,5,4,4],{1:[2,3],2:[3,5],3:[4,5],4:[3,5]},{1:[5,1],2:[5,1]})
#print(CountRegions(x))
#x = Graph([0,1,2,3,4,5,6],{2:[1],3:[1],4:[2,0],5:[3]})
#print(x.edgeList,x.weightList)
#x.reverse()
#print(x.edgeList,x.weightList) 
#print(DFS(x,2))
#print(TSort(x))
#validateConnected(x)
#print("Components:",len(Components(x.unDirectional())))
