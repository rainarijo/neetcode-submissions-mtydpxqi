class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i=0
        new=""
        s=s.lower()
        for ch in s:
            if ch.isalnum():
                new+=ch

        return new==new[::-1]
