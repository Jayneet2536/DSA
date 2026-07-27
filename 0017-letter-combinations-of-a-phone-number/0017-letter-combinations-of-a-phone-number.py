class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = [
            "",      # 0
            "",      # 1
            "abc",   # 2
            "def",   # 3
            "ghi",   # 4
            "jkl",   # 5
            "mno",   # 6
            "pqrs",  # 7
            "tuv",   # 8
            "wxyz"   # 9
        ]
        ans = []

        def combination(ind, key):
            nonlocal ans
            nonlocal digits
            nonlocal arr

            if ind == len(digits):
                ans.append(key)
                return

            number = int(digits[ind])
            for char in arr[number]:
                combination(ind + 1, key + char)
        
        combination(0, "")

        return ans