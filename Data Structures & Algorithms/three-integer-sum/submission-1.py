class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-1):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = -nums[i]

                if nums[j] + nums[k] < target: j += 1
                elif nums[j] + nums[k] > target: k -= 1
                else: 
                    res.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1

        return [list(ele) for ele in res]