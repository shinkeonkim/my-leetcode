from collections import Counter

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        cnt = Counter()
        n = len(A)

        assert len(A) == len(B)

        crt = 0

        for i in range(n):
            cnt[A[i]] += 1
            cnt[B[i]] += 1

            if cnt[A[i]] == 2:
                crt += 1
            
            if cnt[B[i]] == 2 and A[i] != B[i]:
                crt += 1
            
            ans.append(crt)
        
        return ans
