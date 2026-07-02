from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            temp = ''.join(sorted(i))
            #aet
            dic[temp].append(i)
            #aet:eat
        res = []
        for group in dic.values():
            res.append(group)
        return res
