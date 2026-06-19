class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mns = []
        mxs = []

        for i in range(len(arrays)):
            mns.append([arrays[i][0], i])
            mxs.append([arrays[i][-1], i])

        mxs.sort(reverse=True)
        mns.sort()

        ret = 0
        for i in range(2):
            for j in range(2):
                if mns[i][1] != mxs[j][1]:
                    ret = max(ret, abs(mxs[j][0] - mns[i][0]))

        print(mxs, mns)
        return ret
