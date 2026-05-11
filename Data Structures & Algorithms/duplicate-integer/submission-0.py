class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers =[]
        for i in range(len(nums)):
            if nums[i] in unique_numbers:
                return True
            if nums[i] not in unique_numbers:
                unique_numbers.append(nums[i])
        return False