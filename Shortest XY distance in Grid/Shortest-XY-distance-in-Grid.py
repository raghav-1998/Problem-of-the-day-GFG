#User function Template for python3

class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here 
        lst_x = []
        lst_y = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'X':
                    lst_x.append([i,j])
                elif grid[i][j] == 'Y':
                    lst_y.append([i,j])
        
        manhattan = N*M

        for i in range(len(lst_x)):
            for j in range(len(lst_y)):
                manhattan = min(manhattan,(abs(lst_x[i][0] - lst_y[j][0]) + abs(lst_x[i][1] - lst_y[j][1])))
                if manhattan == 1:
                    break
        return manhattan
        