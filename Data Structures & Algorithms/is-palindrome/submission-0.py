class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=0
        
        li=[ch.lower() for ch in s if ch.isalnum()]
        e=len(li)-1
        while b<e:
            if li[b] != li[e]:
                return False
            b+=1
            e-=1
        return True
        