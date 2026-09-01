class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if mp1.get(s[i]):
                mp1[s[i]] += 1
            else:
                mp1[s[i]] = 1 

            if mp2.get(t[i]):
                mp2[t[i]] += 1
            else:
                mp2[t[i]] = 1 
        
        # print(mp1, mp2)
        
        for j in range(len(mp1)):
            # print(f'{mp1.get(s[j])} | {mp2.get(t[j])}')
            if mp1.get(s[j]) == mp2.get(s[j]):
                continue
            else: return False
        
        return True