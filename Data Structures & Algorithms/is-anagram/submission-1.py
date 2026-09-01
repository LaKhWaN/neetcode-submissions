class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = {}
        tt = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in st:
                st[i] += 1
            else:
                st[i] = 1
        
        for j in t:
            if j in tt:
                tt[j] += 1
            else:
                tt[j] = 1
        
        if st == tt:
            return True
        
        return False