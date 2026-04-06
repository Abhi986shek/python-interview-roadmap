"""
Graph Representation

Two ways to represent a graph:
    1. Adjacency Matrix  - 2D array, cell [i][j] = 1 if edge exists
    2. Adjacency List    - dictionary of lists, each key holds its neighbors

Adjacency Matrix:
    Space           : O(V²)
    Add edge        : O(1)
    Check edge      : O(1)
    Get neighbors   : O(V)

Adjacency List:
    Space           : O(V + E)
    Add edge        : O(1)
    Check edge      : O(degree of vertex)
    Get neighbors   : O(degree of vertex)
"""


class GraphMatrix:
    def __init__(self, vertices):
        self.v = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, directed=False):
        if u >= self.v or v >= self.v:
            raise IndexError("Vertex index out of range.")
        self.matrix[u][v] = 1
        if not directed:
            self.matrix[v][u] = 1

    def display(self):
        print("ADJACENCY MATRIX:")
        for row in self.matrix:
            print(row)


class GraphList:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, directed=False):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)

    def display(self):
        print("ADJACENCY LIST:")
        for vertex, neighbors in self.adj.items():
            print(f"  {vertex} -> {neighbors}")


def main():
    print("SELECT REPRESENTATION:")
    print("1. ADJACENCY MATRIX")
    print("2. ADJACENCY LIST")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))

        directed = input("IS THE GRAPH DIRECTED? (y/n): ").strip().lower() == 'y'

        if choice == 1:
            v = int(input("ENTER NUMBER OF VERTICES: "))
            if v <= 0:
                raise ValueError("Vertices must be greater than 0.")
            g = GraphMatrix(v)
            e = int(input("ENTER NUMBER OF EDGES: "))
            for _ in range(e):
                u, v_node = map(int, input("ENTER EDGE (u v): ").split())
                g.add_edge(u, v_node, directed)
            g.display()

        elif choice == 2:
            g = GraphList()
            e = int(input("ENTER NUMBER OF EDGES: "))
            for _ in range(e):
                u, v_node = input("ENTER EDGE (u v): ").split()
                g.add_edge(u, v_node, directed)
            g.display()

        else:
            print("INVALID CHOICE")

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
