#994 Leet Code

from collections import deque
class Solution:
    def contamina(self, lin, col, grid, contaminados, number_contaminados):
        moves = [(lin-1, col), (lin, col+1), (lin+1, col), (lin, col-1)]

        for move in moves:
            x = move[0]
            y = move[1]
            if grid[x][y] == 1:
                grid[x][y] = 2
                contaminados.append([x, y])
                number_contaminados += 1
    
        return number_contaminados
                

    def orangesRotting(self, grid: list[list[int]]) -> int:
        lin = len(grid)
        col = len(grid[0])

        correction_lin = [0 for i in range(col)]
        grid.append(correction_lin)
        for i in range(lin):
            grid[i].append(0)
        
        contaminados = deque()
        nao_contaminados = 0

        for i in range(lin):
            for j in range(col):
                if grid[i][j] == 2:
                    contaminados.append([i, j])
                if grid[i][j] == 1:
                    nao_contaminados += 1

        tam_atual = len(contaminados)
        passos = 0
        while contaminados and nao_contaminados > 0:
            point = contaminados.popleft()
            nao_contaminados -= self.contamina(point[0], point[1], grid, contaminados, 0)
            tam_atual -= 1
            if tam_atual == 0:
                passos += 1
                tam_atual = len(contaminados)

            elif nao_contaminados == 0:
                passos += 1


        if nao_contaminados == 0:
            return passos
        else:
            return -1
        
        


s = Solution()

print(s.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))



        
