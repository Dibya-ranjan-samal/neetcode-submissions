class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):
            element = nums[i]
            if element in dict:
                dict[element] += 1
            else:
                dict[element] = 1    
                
        ans = []

        sorted_freq = sorted(dict , key = dict.get , reverse = True)

        for i in range(k):
            ans.append(sorted_freq[i])

        return ans
        