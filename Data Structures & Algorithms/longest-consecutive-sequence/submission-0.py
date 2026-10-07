class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set(nums)
        longest = 0

        for i in nums:

            if i - 1 not in seen:

                count = 1

                while i + count in seen:
                    count+= 1
                

            longest = max(longest,count)    
        return longest



        