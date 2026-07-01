class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def capacityShip(weights,mid,days):
            curr = 0
            days_needed = 1
            for i in range(len(weights)):
                if curr + weights[i] > mid:
                    days_needed += 1
                    curr = 0
                curr += weights[i]

            return days_needed <= days



        s = max(weights)
        e = sum(weights)
        ans = 0
        while(s <= e):
            mid = (s+e) // 2
            if capacityShip(weights,mid,days):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans
