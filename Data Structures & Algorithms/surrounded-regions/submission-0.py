class Solution:

    def exploreCorners(self, m, n, board, explored):
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # First produce corners
        corners = set()
        for i in range(m):
            corners.add((i, 0))
            corners.add((i, n-1))
        for j in range(n):
            corners.add((0, j))
            corners.add((m-1, j))
        explored.union(corners)
        
        # Then BFS
        queue = list(corners)
        while queue:
            x,y = queue.pop()
            for dx, dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and \
                (x + dx, y + dy) not in explored:
                    if board[x][y] == "O" and board[x + dx][y + dy] == "O":
                        # New point to explore
                        explored.add((x + dx, y + dy))
                        queue.append((x + dx, y + dy))

    def solve(self, board: List[List[str]]) -> None:
        explored = set()
        # All on the edges.
        if len(board) <= 2 or len(board[0]) <= 2: return

        m, n = len(board), len(board[0])
        # First cross whole corner
        self.exploreCorners(m, n, board, explored)

        # Then, mark everything NOT IN EXPLORED from intern as X
        for i in range(1, m-1):
            for j in range(1, n-1):
                if (i,j) not in explored:
                    # We do not need to add to explored now
                    board[i][j] = "X"

