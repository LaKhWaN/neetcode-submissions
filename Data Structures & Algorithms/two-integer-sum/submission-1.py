class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            
            compliment = target - nums[i]
            
            exists = mp.get(compliment)
            if exists is not None:
                return [exists, i]
            else:
                mp[nums[i]] = i
        
        return [-1,-1]