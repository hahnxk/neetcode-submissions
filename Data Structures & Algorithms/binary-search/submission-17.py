class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Idea:
        # 1. Initialize first, middle, and last index. 
        # 2. Search first half and second half of list. 
        #    If target is in first half, set last index to be old middle.
        #    If target is in second half, set first index to be old middle
        # #. Find new middle index and repeat from step 2.
        if target not in nums:
            return -1
        
        start = 0
        end = len(nums) - 1

        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end

        while start < end:
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid
            elif target < mid:
                end = mid
            elif target > mid:
                start = mid