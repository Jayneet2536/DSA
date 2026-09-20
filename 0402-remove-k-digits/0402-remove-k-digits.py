class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st = []

        for n in nums:
            while st and k > 0 and ord(st[-1]) > ord(n):
                st.pop()
                k -= 1
            st.append(n)

        while k != 0:
            st.pop()
            k -= 1
        
        if len(st) == 0:
            return "0"

        ans = "".join(st)
        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        
        ans = ans[i:]
        return ans if ans else '0'

            
                
            

