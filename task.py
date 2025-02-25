
import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self, size):
        self.N = size
        self.grid = self.generate_grid()
        self.source = self.random_cell()
        self.goal = self.random_cell()
        while self.source == self.goal: 
            self.goal = self.random_cell()
        
        self.path = []
        self.topo_order = []
        self.visited = set()

    def generate_grid(self):
        grid = []
        for i in range(self.N):
            row = [random.choice([0, 1])
            for j in range(self.N)]
            grid.append(row)
        return grid


    def random_cell(self):
       
        while True:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if self.grid[x][y] == 1:
                return Node(x, y, 0)

    def dfs(self, node):
        
        if (node.x, node.y) in self.visited:
            return
        self.visited.add((node.x, node.y))
        self.path.append((node.x, node.y))
        self.topo_order.append((node.x, node.y))

        if node.x == self.goal.x and node.y == self.goal.y:
            return

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        for dx, dy in moves:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.N and 0 <= ny < self.N and self.grid[nx][ny] == 1:
                self.dfs(Node(nx, ny, node.depth + 1))

    def display_grid(self):
        
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) == (self.source.x, self.source.y):
                    print(" S ", end="")
                elif (i, j) == (self.goal.x, self.goal.y):
                    print(" G ", end="")
                else:
                    print(f" {self.grid[i][j]} ", end="")
            print()
        print()

    def run(self):
      
        print(f"Grid size: {self.N}*{self.N}")
        self.display_grid()

        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")

        self.dfs(self.source)

        if (self.goal.x, self.goal.y) in self.path:
            print("\nDFS Path:")
            print(" --> ".join(map(str, self.path)))
        else:
            print("\nNo path found from Source to Goal.")

        print("\nTopological Order of Traversal:")
        print(" --> ".join(map(str, self.topo_order)))


grid_size = random.randint(4, 7)
dfs_solver = DFS(grid_size)
dfs_solver.run()
