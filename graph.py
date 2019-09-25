import numbers
from validate import *
from traversal import *
from miscellaneous import *
from properties import *

class Graph:

    def addVertex(self,ver):
        self.vertex.add(ver)
        self.vertexCount+=1

    def addEdge(self,i,j,weight=0):
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
            
    def unDirectional(self):
        unGraph = uniGraph(self.vertexList,self.adjList,self.weightList)
        return unGraph
        #self.vertexList = unGraph.vertexList
        #self.adjList = unGraph.adjList
        #self.weightList = unGraph.weightList
        #del unGraph

    def reverse(self):
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
                raise Exception("Vertex list and Weight List contains different number of elements")

        self.weightList = dict()
        for vertex in adjList.keys():
            self.weightList[vertex] = [0 for conVertex in adjList[vertex]]



        for vertex in weightList:
            for (index,weight) in enumerate(weightList[vertex]):
                self.weightList[vertex][index] = weight

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



            

class uniGraph(Graph):
    def addEdge(self,i,j,weight=0):
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
                #self.addEdge(nbrVertex,vertex,0)
                self.edgeCount += 1
                try:
                    assert weightList[vertex][adjList[vertex].index(nbrVertex)]==weightList[nbrVertex][adjList[nbrVertex].index(vertex)]
                except AssertionError:
                    print("v1:",vertex,", v2:",nbrVertex)
                    print("w1:",weightList[vertex][adjList[vertex].index(nbrVertex)]," ,w2:",weightList[nbrVertex][adjList[nbrVertex].index(vertex)])
                    raise Exception("Ambiguous Weight List")
                except KeyError:
                    print("hi","neglecting an error")

        for vertex in self.vertexList:
            if vertex not in self.adjList:
                self.adjList[vertex]=[]

        try:
            for vertex,nbrWeightList in weightList.items():
                if len(nbrWeightList)> len(adjList[vertex]):
                    raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))
        except:
            raise Exception("Invalid Weight List corresponding to vertex {}".format(vertex))        
        #print("check",self.adjList,weightList)

        for vertex,neighborhood in self.adjList.items():
            for nbrVertex in neighborhood:
                
                ind_vertex = self.adjList[nbrVertex].index(vertex)
                ind_nbrVertex = self.adjList[vertex].index(nbrVertex)
                try:
                    w = weightList[vertex][self.adjList[vertex].index(nbrVertex)]
                except:
                    try:
                        w = weightList[nbrVertex][self.adjList[nbrVertex].index(vertex)]
                    except:
                        w=0
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





#def sortWeight(obj):

                
                
x = Graph([1,2,3,5,4],{1:[2,3],2:[1],4:[5]},{1:[5,1],2:[5]})
x.addEdge(2,5)
#x.addEdge(1,2,8)
#print(CountRegions(x))
#x = Graph([0,1,2,3,4,5],{2:[1],3:[1],4:[2,0],5:[3]})
#print(x.adjList,x.weightList)
#print(x.adjList)
#x.reverse()
print(x.adjList,x.weightList)

#print(x.adjList,x.weightList) 
#print(DFS(x,2))
#print(TSort(x))

#validateTSort(x,exception=False,warning=True)
#print(x.adjList)
#print("Components:",len(Components(x.unDirectional())))
#print("Components:",len(Components(x)))
#print(x.adjList,x.weightList)