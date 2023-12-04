from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answers = [1] * n
        # Use answers as the Prefix product array
        for i in range(1, n):
            answers[i] = answers[i - 1] * nums[i - 1]
        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answers[i] *= suffix
            suffix *= nums[i]

        return answers