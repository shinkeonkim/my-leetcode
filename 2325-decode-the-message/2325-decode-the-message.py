class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}

        key = key.replace(" ", "")
        crt = 0
        for i in key:
            if i in d:
                continue

            d[i] = chr(crt + 97)
            crt += 1

        ans = ""
        for i in message:
            if i in d:
                ans += d[i]
            else:
                ans += i

        return ans
