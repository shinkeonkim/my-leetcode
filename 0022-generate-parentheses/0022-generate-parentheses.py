class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stats = [''] * (2 * n)
        ans = []

        def f(n, current, open_count, close_count):
            if current == (2 * n):
                ans.append("".join(stats[::]))
                return

            if open_count < n:
                stats[current] = '('
                f(n, current + 1, open_count + 1, close_count)
                stats[current] = ''

            if close_count < n and close_count < open_count:
                stats[current] = ')'
                f(n, current + 1, open_count, close_count + 1)
                stats[current] = ''

        f(n, 0, 0, 0)

        return ans
