class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))

        ans = [
            [arr[i - 1], arr[i]]
            for i in range(1, len(arr))
            if mn == arr[i] - arr[i - 1]
        ]

        return ans
