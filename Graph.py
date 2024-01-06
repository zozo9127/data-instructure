class Graph:
    def __init__(self , n):
        self.size = n
        self.M = []
        for i in range (n):
            self.M.append([0 for j in range (n)])

    def add_edge(self , v1 , v2):
        self.M[v1][v2] = 1
        self.M[v2][v1] = 1

    def display(self):
        for i in range (self.size):
            for j in range (self.size):
                print(self.M[i][j])
            print()

