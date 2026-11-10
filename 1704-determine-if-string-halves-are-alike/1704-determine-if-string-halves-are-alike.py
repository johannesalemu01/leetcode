class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      n=len(s)
      vowels={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}   
      count_a=0
      count_b=0
      a=s[0:n//2]
      b=s[n//2:]

      for char in a:
        if char in vowels:
            count_a+=1

      for char in b:
        if char in vowels:
            count_b+=1      

      return count_a==count_b      


