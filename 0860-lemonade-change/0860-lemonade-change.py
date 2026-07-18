from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = Counter()

        for bill in bills:
            if bill == 5:
                count[5] += 1
                continue

            if bill == 10:
                if count[5] == 0:
                    return False

                count[5] -= 1
                count[10] += 1
                continue

            if bill == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                    continue

                if count[10] == 0 and count[5] > 2:
                    count[5] -= 3
                    continue

                return False

        return True
