class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for curr in strs:
            key = "".join(sorted(curr))
            #aet
            if key in dic:
                #dic[key] = [curr]
                #aet:[eat]
                dic[key] = [curr]
