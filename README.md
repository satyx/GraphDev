# GraphDev
*A Python library for implementing graph data structure and standard algorithms for development purposes*

#### Dependency
* Python >= 3.0
#### Features
* One Line instance creation of graph and its attributes
  * Adjacency List
  * Vertex List
  * Weight List
* Special class for undirectional graph
* Calculation of various non trivial features of graph including number of **components, regions**, etc
* Nature detection:
  * Directed/Non-Directed
  * Cyclic/Non-Cyclic
  * Connected/Disconnected/Weakly Connected
* Graph Traversal via BFS and DFS
* Topological Sorting
* Customised Error Classes
* Inclusion of multiple validation functions having options for raising error or warning or returning Truth Value along with optional custom message to be displayed
* Generation of MST (Minimum Spanning Tree) using Kruskal's Algorithm
* Minimum Distance determination using standard algorithms:
  * Dijkstra, additionally it also returns the parent of each vertex lying on the path from source to desired vertex enabling the *path determination*
  * Bellman Ford 
  * Floyd Warshall
