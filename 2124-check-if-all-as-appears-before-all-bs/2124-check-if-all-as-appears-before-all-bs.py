class Solution:
    def checkString(self, s: str) -> bool:

        first_b_index=s.find('b')

        for index in range(first_b_index,len(s)):
            if 'b' in s and s[index]=='a':
                return False

        return True        
