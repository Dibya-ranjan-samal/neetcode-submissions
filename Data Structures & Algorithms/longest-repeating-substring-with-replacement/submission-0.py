class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left ,right = 0,0
        maxlen = 0
        maxf = 0
        freq = {}
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            maxf = max(maxf, freq[s[right]])

            if ((right - left + 1) - maxf) > k:
             freq[s[left]] -= 1
             left += 1 

            maxlen = max(maxlen , right - left + 1)

        return maxlen
        