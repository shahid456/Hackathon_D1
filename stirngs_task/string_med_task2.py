class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.replace(' ','')
        s_op=[]
        s_val=[]
        curr=""
        prev=""
        x=0
        while x <(len(s)):
            if s[x].isdigit():
                curr+=s[x]
            elif s[x] in ['+','-','*','/']:
                if s[x] in ['+','-']:
                    s_op.insert(0,s[x])
                    if curr!="":
                        s_val.insert(0, int(curr))
                    else:
                        s_val.insert(0,int(prev))
                    prev=curr
                    curr=""
                else:
                    if curr=="":
                        curr=prev
                    op=s[x]
                    x+=1
                    temp=""
                    while x<len(s) and s[x].isdigit():
                        temp+=s[x]
                        x+=1
                    x-=1
                    if op=='*':
                        curr=str(int(temp)*int(curr))
                    else:
                        curr=str(int(curr)//int(temp))
                        prev=curr
                        curr=""
            x+=1

        if curr!="":
            s_val.insert(0,int(curr))
        else:
            s_val.insert(0,int(prev))
        j=-1
        result=0
        pre=s_val.pop()
        result=pre
        while s_val!=[]:
            cur=s_val.pop()
            oprt=s_op.pop()
            if oprt=='+':
                result=pre+cur
                pre=result
            else:
                result=pre-cur
                pre=result
        return result






A=Solution()
print(A.calculate("14/3*2"))
