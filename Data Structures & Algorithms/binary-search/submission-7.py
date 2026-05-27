class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check if the target number exists in nums list
        if target not in nums:
            return -1
        
        # Create start and end index for binary search
        start = 0
        end = len(nums) - 1

        # If target is start or end index, return index
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        # Loop through nums list from start to end index
        while start <= end:
            # Find middle index between start and end index
            mid_index = (end + start) // 2
            # Check if target equal to halfway point and if yes, return
            if target == nums[mid_index]:
                    return mid_index
            # If target is in first half of list
            if target in nums[start: mid_index]:
                # Change end index to halfway point of current list
                end = mid_index
            # If target is in second half of list
            elif target in nums[mid_index: end]:
                # Change start index to halfway point of current list
                start = mid_index