class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def check(brac, opn, cls):

            if opn == cls and opn==n:
                result.append(brac)
                return
            if opn < n:
                check(brac+"(", opn+1, cls)

            if cls < opn:
                check(brac+")", opn, cls+1)


        check("",0,0)
        return result

A=Solution()
print(A.generateParenthesis((3)))