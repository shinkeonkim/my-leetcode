from collections import Counter
class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        # 일단 naive 한 풀이로 하고 제약조건을 해결해보자
        count = Counter(nums)
        ans = [0, 0]
        for k, v in count.items():
            if v == 1:
                ans[0] = k
            if v == 2:
                ans[1] = k

        return ans
