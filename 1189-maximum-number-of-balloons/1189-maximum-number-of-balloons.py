class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        char_count=Counter(text)
        
        target=Counter("balloon")
        min_count=float('inf')

        for char in target:
            min_count = min(min_count, char_count[char] // target[char]) 
            # // used to handle the single o's and l's

        return min_count        


       