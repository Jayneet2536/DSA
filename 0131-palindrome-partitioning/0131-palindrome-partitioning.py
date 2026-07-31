class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(ind, res):
            if ind == len(s):
                ans.append(res[:])
                return
            
            for i in range(ind, len(s)):
                if is_palindrome(s, ind, i):
                    res.append(s[ind:i+1])
                    dfs(i+1, res)
                    res.pop()

        def is_palindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True

        ans = []
        dfs(0, [])

        return ans
