
class Solution:
    def isWordExist(self, board, word):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            visited[row][col] = True

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if (
                    0 <= new_row < len(board)
                    and 0 <= new_col < len(board[0])
                    and not visited[new_row][new_col]
                    and board[new_row][new_col] == word[idx]
                ):
                    if dfs(new_row, new_col, idx + 1):
                        return True

            visited[row][col] = False

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False
