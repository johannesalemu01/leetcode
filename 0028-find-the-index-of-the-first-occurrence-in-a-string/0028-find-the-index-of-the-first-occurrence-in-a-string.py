class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack=haystack.lower()
        needle=needle.lower()

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1  