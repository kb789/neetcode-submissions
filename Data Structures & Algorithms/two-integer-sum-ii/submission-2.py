class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        beg = 0
        end = 1
        while end<len(numbers):
            if numbers[beg]+numbers[end]==target:
                return [beg+1, end+1]
            if end==len(numbers)-1:
                beg=beg+1
                end=beg+1
            else:
                end+=1


        