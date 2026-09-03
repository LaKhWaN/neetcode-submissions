class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mp = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        for i in s:
            if i in ('[', '{', '('): stack.append(i)
            elif stack: 
                ele = stack.pop()
                if i != mp.get(ele): return False
            else: return False
            # print(i, stack)

        if stack: return False
        return True