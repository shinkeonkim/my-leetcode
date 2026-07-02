class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def to_label(rank):
            if rank == 1:
                return "Gold Medal"

            if rank == 2:
                return "Silver Medal"

            if rank == 3:
                return "Bronze Medal"

            return str(rank)

        data = [
            [i, score[i], 0]
            for i in range(len(score))
        ]  # idx, score, rank

        data.sort(key=lambda t: -t[1])

        for i in range(len(data)):
            data[i][2] = i + 1

        data.sort(key=lambda t: t[0])

        return [to_label(datum[2]) for datum in data]
