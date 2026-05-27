class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap Solution
        hashMap = {}
        # Loop through nums
        for i in range(len(nums)):
            # Find the difference between target and num
            diff = target - nums[i]
            # If difference exists already in hashMap, return both indices
            if hashMap.get(diff) != None:
                return [hashMap.get(diff), i]
            # If diff doesn't exist, add nums[i] to the hashMap with (value, index)
            hashMap[nums[i]] = i