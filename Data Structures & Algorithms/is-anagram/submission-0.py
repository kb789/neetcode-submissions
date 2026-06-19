class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        for ch in s:
            if ch in s_dict.keys():
                s_dict[ch]+=1
            else:
                s_dict[ch]=1
        for ch in t:
            if ch in t_dict.keys():
                t_dict[ch]+=1
            else:
                t_dict[ch]=1
        if s_dict==t_dict:
            return True
        else:
            return False 