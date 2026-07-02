class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum == right_sum:
                return i
        return -1
