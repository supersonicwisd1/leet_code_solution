"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        num_of_weeks = n // 7
        num_of_days = n%7
        bal = 0
        fd = 1
        if n == 0:
            return 0
        elif n < 7:
            for x in range(1, n+1):
                bal += x
            return bal
        else:
            wb = self.calculate_for_weeks(num_of_weeks)
            db = self.calculate_for_days(num_of_days, num_of_weeks)
            bal = wb + db
            return bal
        
    def calculate_for_weeks(self, num_of_weeks:int) -> int:
        bal = 0 
        for x in range(1, num_of_weeks+1):
            for y in range(x, x+7):
                bal += y
        return bal 
    
    def calculate_for_days(self, num_of_days:int, num_of_weeks:int) -> int:
        bal = 0
        for x in range(num_of_weeks + 1, num_of_days+num_of_weeks+1):
            bal += x
        return bal

sol = Solution()
print(sol.totalMoney(10))