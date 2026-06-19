class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_dict={}
        for num in nums:
            if num in test_dict.keys():
                return True
            else:
                test_dict[num]=1
        return False