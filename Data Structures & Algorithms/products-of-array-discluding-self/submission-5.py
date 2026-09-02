class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        total1 = 1
        total2 = 1
        for n in nums:
            total1 *= n
            arr1.append(total1)

        for i in range(len(nums) - 1, -1, -1):
            total2 *= nums[i]
            arr2.append(total2)
        
        arr2.reverse()
        # print(arr1, arr2)

        ans = []
        ans.append(arr2[1])
        for i in range(1, len(nums)-1):
            ans.append(arr1[i-1]*arr2[i+1])
        
        ans.append(arr1[len(arr1)- 2])
        # print(ans)
        return ans
