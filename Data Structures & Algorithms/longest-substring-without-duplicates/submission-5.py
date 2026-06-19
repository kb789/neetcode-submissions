class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        max_win=[s[0]]   
        l = len(s)   
        max_len=1   
        i=1        
        while i < l:
            if s[i] not in max_win:
                max_win.append(s[i])
                i+=1
            else:
                max_len=max(len(max_win), max_len)
                max_win=max_win[1:] 
           
        max_len=max(len(max_win), max_len)   
        return max_len
    

