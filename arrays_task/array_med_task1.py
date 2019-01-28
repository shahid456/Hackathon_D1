class Solution:
    def leastInterval(self, tasks=[], n=0):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        s=set(tasks)
        cnt=[]
        for x in s:
            cnt.append(tasks.count(x))
        result=0
        while sum(cnt)>0:
            t=0
            j=0
            cnt=sorted(cnt,reverse=True)
            while j<(len(cnt)):
                if cnt[j]!=0:
                    cnt[j]-=1
                    t+=1
                j+=1
                if t==n+1:
                    cnt=sorted(cnt,reverse=True)
                    result+=t
                    j=0
                    t=0

            if t<n+1 and sum(cnt)!=0:
                result=result+t+(n+1-t)
            else:
                result+=t
        return result
A=Solution()
print(A.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))


