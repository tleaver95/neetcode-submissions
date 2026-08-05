class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]

        for col in nums:
            colors[col] += 1

        j = 0
        i = 0
        while i < len(nums):
            if colors[j] > 0:
                colors[j] -= 1
                nums[i] = j
                i += 1
            else:
                j += 1
            
