#Graphs can be represented by adjacency matrix and adjacency list
'''
    B
  /  \
A --- C
 \
  \
   D
   consider the graph

'''

# vertex=['A','B','C','D']
#
# adjecency_matrix=[
#     [0,1,1,1],#A
#     [1,0,1,0],#B
#     [1,1,0,0],#C
#     [1,0,0,0]#D
# ]

#Class implementation

class Graph:
    def __init__(self,size):
        self.adj_matrix=[[0]*size for _ in range(size)]
        self.size=size
        self.vertex_data=[''] * size

    def add_edge(self,u,v,weight=1):
        if 0<=u <self.size and 0<=v<self.size:
            self.adj_matrix[u][v]=weight

    def add_vertex(self,vertex,data):
        if 0 <= vertex <self.size:
            self.vertex_data[vertex]=data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0',row)))
        print("Vertex Data:")
        for vertex,data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}:{data}")

    # Traverasals DFS and BFS
    def dfs_util(self,v,visited):
        visited[v]=True
        print(self.vertex_data[v],end=' ')
        for i in range(self.size):
            if self.adj_matrix[v][i]==1 and not visited[i]:
                self.dfs_util(i,visited)
    def dfs(self,start_vertex_data):
        visited=[False] * self.size
        start_vertex=self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex,visited)

    def bfs(self,start_vertex_data):
        queue=[self.vertex_data.index(start_vertex_data)]
        visited=[False]*self.size
        visited[queue[0]]=True

        while queue:
            current_vertex=queue.pop(0)
            print(self.vertex_data[current_vertex],end=' ')

            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i]=True



g=Graph(7)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_vertex(4,'E')
g.add_vertex(5,'F')
g.add_vertex(6,'G')

g.add_edge(3,0)
g.add_edge(3,4)
g.add_edge(4,0)
g.add_edge(0,2)
g.add_edge(2,5)
g.add_edge(2,6)
g.add_edge(5,1)
g.add_edge(1,2)


g.print_graph()
g.dfs('D')
print()
g.bfs('D')


