class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s=Counter(s)
        counter_t=Counter(t)

        for char,value in counter_t.items():
            if char not in counter_s:
                return char
            if counter_s[char]!=value:
                return char   