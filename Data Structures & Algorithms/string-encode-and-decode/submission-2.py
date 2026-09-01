class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "None"
        s = ";".join(strs)
        return s
    def decode(self, s: str) -> List[str]:
        return s.split(";") if s != "None" else []