class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sum =0
        arr.sort()
        min=int(0.05*len(arr))
        max=int(0.05*len(arr))

        new_arr=arr[min:len(arr)-max]
        # print(new_arr)
        # print(f"min={min}")
        # print(f"max={max}")
        for num in new_arr:
            sum +=num

        return sum/len(new_arr)    
        