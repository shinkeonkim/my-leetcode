class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def find_winner(ar):
            if all(ar[0][0] == ar[i][i] != 0 for i in range(3)):
                return ar[0][0]

            if all(ar[2][0] == ar[2 - i][i] != 0 for i in range(3)):
                return ar[2][0]

            for i in range(3):
                if all(ar[i][j] == ar[i][0] != 0 for j in range(3)):
                    return ar[i][0]

                if all(ar[j][i] == ar[0][i] != 0 for j in range(3)):
                    return ar[0][i]

            return 0


        grid = [[0] * 3 for _ in range(3)]

        crt = 1
        for move in moves:
            grid[move[0]][move[1]] = crt
            crt = 3 - crt

            winner = find_winner(grid)

            if winner:
                return ['', 'A', 'B'][winner]

        print(*grid, sep="\n")

        if len(moves) < 9:
            return 'Pending'

        return 'Draw'
