class Solution:
    def isPalindrome(self, s: str) -> bool:
        pt1=0
       
        s=s.lower()
        s = "".join(char for char in s if char.isalnum())
        pt2=len(s)-1
        print(s)
        while pt1<pt2:
            if s[pt1]!=s[pt2]:
                return False
            pt1+=1
            pt2-=1
        return True