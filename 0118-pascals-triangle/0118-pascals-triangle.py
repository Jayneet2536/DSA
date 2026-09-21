class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []

        for r in range(numRows):
            row = [1] * (r + 1)

            for j in range(1, r):
                row[j] = ans[r - 1][j - 1] + ans[r - 1][j]

            ans.append(row)

        return ans