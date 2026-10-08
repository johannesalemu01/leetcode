class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum=0
        while left<=right:
            if left==right:
                sum+=self.nums[left]
            else:    
                sum+=self.nums[left]+self.nums[right]
            left+=1
            right-=1

        return sum    

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)