class Solution:
    def maxProduct(self, n: int) -> int:
        k = n
        secondlargest = -1
        largest = -1
        nums = []
        while k != 0:
            digit = k % 10
            k = k // 10
            if digit > largest:
                secondlargest = largest
                largest = digit
                continue
            elif digit > secondlargest:
                secondlargest = digit
                continue
        
        return largest * secondlargest