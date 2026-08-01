class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for curr in strs:
            key = "".join(sorted(curr))
            #aet
            if key in dic:
                # EXAMPLE -> dic[key] = [curr]
                dic[key] = [curr]
