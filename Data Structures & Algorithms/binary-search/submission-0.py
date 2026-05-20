class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check if the target number exists in nums list
        if target not in nums:
            return -1
        
        start = 0
        end = len(nums) - 1

        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        while start <= end:
            mid_index = (end + start) // 2
            if target in nums[start: mid_index]:
                end = mid_index
                if target == nums[mid_index]:
                    return mid_index
            elif target in nums[mid_index: end]:
                start = mid_index
                if target == nums[mid_index]:
                    return mid_index