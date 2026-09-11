class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]

        while l < r:
            mid = (l+r) // 2

            total_hours = 0
            for i in range(len(piles)):
                hours = math.ceil(piles[i]/mid)
                total_hours += hours

            if total_hours > h: l = mid + 1
            else: r = mid
        
        return l