class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        day = 1
        current_money = 1
        while day <= n:
            total += current_money
            current_money += 1
            if day % 7 == 0:
                current_money -= 6  # On Mondays, reset to $1 more than the previous Monday
            day += 1
        return total

sol = Solution()
print(sol.totalMoney(100000))
