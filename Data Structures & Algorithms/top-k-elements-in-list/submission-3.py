class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = range(1,len(nums)+1)

        buckets = {key: [] for key in keys}
        my_set=set(nums)
        
        for s in my_set:
            x = nums.count(s)
            buckets[x].append(s)
        print(buckets)
        key_list=list(buckets.keys())
        count=0
        ind=len(key_list)-1
        ans=[]
        while count<k and ind > -1:
            if buckets[key_list[ind]] != []:
                
                for item in buckets[key_list[ind]]:
                    ans.insert(0, item)
                    count+=1
            ind-=1
        return ans
        
        
