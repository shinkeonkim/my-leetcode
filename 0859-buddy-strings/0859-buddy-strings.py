from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            if len(set(s)) == len(s):
                return False

            return True

        differencies = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differencies.append([s[i], goal[i]])

        if len(differencies) != 2:
            return False

        if differencies[0][0] != differencies[1][1] or differencies[0][1] != differencies[1][0]:
            return False

        return True
