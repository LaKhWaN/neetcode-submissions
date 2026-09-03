class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = collections.deque()

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stk.append(int(token))
            else:
                b = int(stk.pop())
                a = int(stk.pop())

                # print(a,token,b)
                ans = None
                if token == "+": ans = a + b
                elif token == "-": ans = a - b
                elif token == "*": ans = a * b
                else: ans = a / b

                stk.append(ans)
        
        # print(stk)
        return int(stk[0])
