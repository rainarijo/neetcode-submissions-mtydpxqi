class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        hash_map={}
        max_len=0
        n=len(s)

        for r in range(n):
            if s[r] in hash_map and hash_map[s[r]]>=l:
                l=hash_map[s[r]]+1
            
            hash_map[s[r]]=r
            max_len=max(max_len,r-l+1)
        return max_len