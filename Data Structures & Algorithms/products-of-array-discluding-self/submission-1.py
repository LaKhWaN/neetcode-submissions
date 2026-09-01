class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        result = []

        res = 1
        for num in nums:
            res = num*res
            prefix.append(res)

        res = 1
        for n in range(len(nums) - 1, -1, -1):
            res *= nums[n]
            postfix.insert(0,res)
        
        prefix.append(1)
        postfix.insert(0,1)
        # print(prefix)
        # print(postfix)

        for i in range(1, len(nums)+1):
            prfx = prefix[i-1]
            pstfx = postfix[i+1]
            # print(f"prfx: {prfx}, pstfx: {pstfx}")
            result.append(prfx*pstfx)
        
        return result