class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0 
        ret = 0
        mapping = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        checker = [
            ('I', ('V', 'X')),
            ('X', ('L', 'C')),
            ('C', ('D', 'M')),
        ]

        while i < len(s):
            if i + 1 < len(s):
                flag = False
                for chk, chk2s in checker:
                    if s[i] == chk and s[i + 1] in chk2s:
                        ret += mapping[s[i + 1]] - mapping[s[i]]
                        i += 2
                        flag = True
                        break
                
                if flag:
                    continue
            
            ret += mapping[s[i]]            
            i += 1
        return ret



