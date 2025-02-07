from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 0
        
        if digits[-1] == 9:
            joined_digits = int("".join(str(num) for num in digits))
            joined_digits += 1
            return [int(digit) for digit in str(joined_digits)]
        digits[-1] += 1
        return digits