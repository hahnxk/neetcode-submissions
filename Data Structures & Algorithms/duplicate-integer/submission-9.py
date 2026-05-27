class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a Hash Set
        # (Python sets are built-in implementations of hash sets)
        hashSet = set()

        # Loop through list of nums
        for num in nums:
            # If duplicate found, return True
            if num in hashSet:
                return True
            # Else add num to hashSet
            hashSet.add(num)
        # If no duplicates, return False
        return False