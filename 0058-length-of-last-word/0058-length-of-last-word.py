class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        word_list=s.split(" ")
        last_word=word_list.pop()
        return len(last_word)