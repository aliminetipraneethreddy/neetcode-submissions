from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            group = []

            for j in range(i, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True

            a.append(group)

        return a