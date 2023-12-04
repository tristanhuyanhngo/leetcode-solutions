from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_even_digits = 0
        for number in nums:
            count_digits = 0
            while number != 0:
                number //= 10
                count_digits += 1
            if count_digits % 2 == 0:
                count_even_digits += 1
        
        return count_even_digits