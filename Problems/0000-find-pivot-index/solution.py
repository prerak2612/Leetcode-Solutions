class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        for i in range(len(nums)):
