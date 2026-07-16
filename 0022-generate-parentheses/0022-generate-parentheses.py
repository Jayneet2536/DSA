
class Solution:
    def generate(self, s, opn, close, arr, n):
        if opn > n:
            return

        if opn == close and opn + close == 2*n:
            arr.append(s)
            return
        
        self.generate(s + "(", opn + 1, close, arr, n)
        if opn > close:
            self.generate(s + ")", opn, close + 1, arr, n)

    def generateParenthesis(self, n):
        #your code goes here
        arr = []
        self.generate("", 0, 0, arr, n)

        return arr