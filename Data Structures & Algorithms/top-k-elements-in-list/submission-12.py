class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums))]
        mp = {}
        for n in nums:
            if mp.get(n):
                mp[n] += 1
            else:
                mp[n] = 1
        
        # print(mp)
        for key in mp:
            # print(mp.get(key))
            freq[mp.get(key)-1].append(key)
        
        # print(freq)

        res = []

        for j in range(len(freq)-1, -1, -1):
            # print("freq[j]",freq[j])
            if len(freq[j]) == 0:
                continue
            
            for c in freq[j]:
                res.append(c)
                if len(res) == k:
                    return res

        return res