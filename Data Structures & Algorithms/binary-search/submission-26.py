class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Idea:
        # 1. Initialize first, middle, and last index. 
        # 2. Search first half and second half of list. 
        #    If target is in first half, set last index to be old middle.
        #    If target is in second half, set first index to be old middle
        # #. Find new middle index and repeat from step 2.
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end-start) // 2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
