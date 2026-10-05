class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prefix = {}


        for i in range(len(nums)):
            find = target - nums[i]

            if find in prefix:
             return [prefix[find], i]

            prefix[nums[i]] = i

        return []
        