class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        sorted_nums = list(dict.fromkeys(nums))

        print(sorted_nums)
        res = []
        cnt = 1        
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                cnt += 1
    
            else:
                res.append(cnt)
                cnt = 1
        
        
        res.append(cnt)
        return max(res)