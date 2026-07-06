class Solution:
    def validStrings(self, n: int) -> List[str]:
        prevs = ['0', '1']

        for _ in range(2, n + 1):
            crts = []

            for prev in prevs:
                if prev[-1] == '0':
                    crts.append(prev + '1')
                else:
                    crts.extend([prev + '1', prev + '0'])

            prevs = crts

        return prevs
