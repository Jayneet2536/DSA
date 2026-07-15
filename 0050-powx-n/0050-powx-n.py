class Solution:
    def pow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n < 0:
            x = 1 / x
            n *= -1
        if n == 1:
            return x

        if n %2 == 0:
            return pow(x * x, n // 2)
        return x * pow(x, n - 1)


    def myPow(self, x: float, n: int) -> float:
        ans = self.pow(x, n)

        return ans