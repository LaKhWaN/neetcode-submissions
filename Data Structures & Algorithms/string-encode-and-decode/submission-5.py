class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'none'
        return ";;".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'none': return []
        spt = s.split(";;")
        # print(f"s: {s}, spt: {spt}")
        if spt == "":
            return []
        return spt