class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
            max=0
            for words in sentences:
                if len(words.split(" "))>max:
                    max=len(words.split(" "))

            return max    

