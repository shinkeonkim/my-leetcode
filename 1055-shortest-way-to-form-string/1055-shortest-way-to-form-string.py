class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        cnt = 0

        for j in range(len(target)):
            matched = False

            for _ in range(len(source)):
                if source[i] == target[j]:
                    matched = True
                    i = (i + 1) % len(source)

                    if i == 0:
                        cnt += 1
                    break

                i = (i + 1) % len(source)
                if i == 0:
                    cnt += 1

            if matched:
                continue

            return -1

        if i > 0:
            cnt += 1


        return cnt
