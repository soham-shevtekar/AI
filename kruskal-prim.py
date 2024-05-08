from queue import PriorityQueue

def prim(graph,startNode,visited):
    pq=PriorityQueue()
    mstEdges=[]
    mstCost=0

    visited.add(startNode)

    for neighbor,weight in graph[startNode]:
        pq.put((startNode,neighbor,weight))
    
    while not pq.empty() and len(visited)<len(graph):
        src,dest,weight=pq.get()
        
        if dest not in visited:
            visited.add(dest)
            mstEdges.append((src,dest,weight))
            mstCost+=weight
        
            for neighbor,weight in graph[dest]:
                pq.put((dest,neighbor,weight))

    return mstEdges,mstCost


def kruskal(graph):
    mstEdges=[]
    mstCost=0

    edges=sorted((src,dest,weight)for src in graph for dest,weight in graph[src])

    component={node:node for node in graph}

    def find(node):
        while node!=component[node]:
            node=component[node]
        return node
    
    def union(src,dest):
        rootSrc=find(src)
        rootDest=find(dest)
        component[rootSrc]=rootDest
    
    for src,dest,weight in edges:
        if find(src)!=find(dest):
            mstEdges.append((src,dest,weight))
            mstCost+=weight
            union(src,dest)
    
    return mstEdges,mstCost


def setGraph(graph):
    numEdges=int(input("Enter the no. of edges: "))
    for _ in range(numEdges):
        node=input("Enter the node: ")
        edges=input("Enter the neighbor nodes along with their weight separated by space: ").split()
        neighbors=[(edges[i],int(edges[i+1]))for i in range(0,len(edges),2)]
        graph[node]=neighbors

    return graph 


def menu(graph):
    print("\n--------------MENU--------------\n1.Enter graph\n2.Kruskal's algorithm\n3.Prim's algorithm\n4.Exit")
    choice=int(input("\nEnter your choice: "))

    if choice==1:
        setGraph(graph)
        print(graph)
    elif choice==2:
        print("Kruskal's Algorithm: ")
        mstEdges,mstCost=kruskal(graph)
        print(str(mstEdges)+"\n"+str(mstCost))
    elif choice==3:
        print("Prim's Algorithm: ")
        startNode=input("Enter the starting node: ")
        mstEdges,mstCost=prim(graph,startNode,set())
        print(str(mstEdges)+"\n"+str(mstCost))
    else:
        print("Invalid input")



graph={}

while True:
    menu(graph)

# Enter the no. of edges: 8
# Enter the node: A
# Enter the neighbor nodes along with their weight separated by space: B 2 C 4
# Enter the node: B
# Enter the neighbor nodes along with their weight separated by space: A 2 C 3 D 6
# Enter the node: C
# Enter the neighbor nodes along with their weight separated by space: A 4 B 3 D 7
# Enter the node: D
# Enter the neighbor nodes along with their weight separated by space: B 6 C 7 A 1

#Time complexity : O(ELogE)
#Space complexity : DFS BFS :- O(E)


