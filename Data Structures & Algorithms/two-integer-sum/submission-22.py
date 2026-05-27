class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap.get(diff), i]
            prevMap[num] = i