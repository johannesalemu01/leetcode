class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        target=self.wordToNumber(targetWord)
        firstWord=self.wordToNumber(firstWord)
        secondWord=self.wordToNumber(secondWord)

        return firstWord+secondWord==target

    def wordToNumber(self,s:str)->int:
        num_str=""
        for c in s:
            num_str+=str((ord(c)-ord('a')))

        return int(num_str)     