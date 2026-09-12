class Solution:
    def isSorted(self, arr):
        # code here
        left=0
        right =1
        while left<right and right<len(arr):
            if  arr[left]> arr[right]:
               return False
            left +=1
            right +=1
        return True    
            
            