class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={"a","e","i","o","u","A","E","I","O","U"}

        vowel_s=[]

        answer=list(s)

        counter=0

        for char in s[::-1]:
            if char in vowels:
                vowel_s.append(char)

        for i in range(len(s)):
            if s[i] in vowels:
                answer[i]=vowel_s[counter]
                counter+=1

        return "".join(answer)       





