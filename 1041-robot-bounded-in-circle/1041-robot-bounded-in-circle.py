class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def move(y, x, d):
            diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            crt = [y, x]

            for instruction in instructions:
                if instruction == 'G':
                    crt[0] += diff[d][0]
                    crt[1] += diff[d][1]
                elif instruction == 'L':
                    d = (d + 3) % 4
                elif instruction == 'R':
                    d = (d + 1) % 4

            return crt + [d]

        current = [0, 0, 0]
        for _ in range(4):
            current = move(*current)

            print(current)

            if current[0] == current[1] == 0:
                return True

        return False
