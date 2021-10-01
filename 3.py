#Time Complexity = O(N)
#Method = Sliding Window Method
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=set()
        l=0
        c=0
        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l=l+1
            temp.add(s[r])
            c=max(c, r-l+1)
        return c
        
