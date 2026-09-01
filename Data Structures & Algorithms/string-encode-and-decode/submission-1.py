class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        if len(strs) == 0:
            return "None"
        s = ";".join(strs)
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split(";") if s != "None" else []