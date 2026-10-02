class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count_ransom=Counter(ransomNote)
        count_magazine=Counter(magazine)

        for char,count in count_ransom.items():
            if char not in count_magazine:
                return False
            if count>count_magazine[char]:
                return False

        return True            


