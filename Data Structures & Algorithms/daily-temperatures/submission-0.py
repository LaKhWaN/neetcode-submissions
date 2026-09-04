class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque()
        ans = [0] * len(temperatures)
       
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack: 
                ans[i] = 0
            else:
                while stack and temperatures[i] >= stack[-1][0]:
                    stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i
            else:
                ans[i]=0

            stack.append((temperatures[i], i))
        return ans