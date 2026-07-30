class Solution:
    def gatherValidPositions(self, x:int, y:int, m:int, n:int) -> List[Tuple[int,int]]:
        vp = []
        for i in [-1, 1]:
            if 0 <= (x+i) < m:
                vp.append((x+i, y))
        for i in [-1, 1]:
            if 0 <= (y+i) < n:
                vp.append((x, y+i))
        return vp

    def exploreIsland(self, 
                      start: Tuple[int,int],
                      grid: List[List[str]], 
                      explored: Set()) -> None:
        m, n = len(grid), len(grid[0])
        queue = [start]
        while queue:
            x, y = queue.pop()
            for x_adj, y_adj in self.gatherValidPositions(x,y,m,n):
                if (x_adj, y_adj) not in explored and grid[x_adj][y_adj] == "1":
                    explored.add((x_adj, y_adj))
                    queue.append((x_adj, y_adj))

    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in explored:
                    explored.add((i, j))
                    if grid[i][j] == "1":
                        self.exploreIsland((i,j), grid, explored)
                        num_islands += 1
        return num_islands
