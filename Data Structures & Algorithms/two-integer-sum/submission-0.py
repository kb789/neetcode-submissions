class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict={}
        for i in range(0, len(nums)):
            complement = target-nums[i]
            if complement in n_dict.keys():
                ans =  [i, n_dict[complement]]
                ans.sort()
                return ans
            else:
                n_dict[nums[i]]=i

        