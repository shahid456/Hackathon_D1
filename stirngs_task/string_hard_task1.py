class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        n=int(n)
        n_less=int(n)-1
        n_greater=int(n)+1
        while int(n_less)>=0 and len(str(n_greater))<=10:
            n_less=str(n_less)
            n_greater=str(n_greater)
            if n_less==n_less[::-1]:
                return n_less
            if n_greater==n_greater[::-1]:
                return n_greater
            n_less=int(n_less)
            n_greater=int(n_greater)
            n_less-=1
            n_greater+=1
        n=str(n)
        temp=list(n)
        j=-1
        if len(n)%2==0:
            l=int(len(n)/2)

        else:
            l=len(n)//2+1
            l=int(l)
        for x in range(l):
            if temp[j]!=temp[x]:
                temp[j]=temp[x]
            j=j-1
        temp1=n
        j=-1
        t=(int(temp1[0:l])-0)
        temp1=str(t)+n[l:len(n)]
        temp1=list(temp1)
        if len(n)%2==0:
            l=int(len(temp1)/2)
        else:
            l=len(temp1)//2+1
            l=int(l)
        for x in range(l):
            if temp1[j]!=temp1[x]:
                temp1[j]=temp1[x]
            j=j-1
        s1=""
        s2=""
        for x in temp1:
            s1+=x
        for x in temp:
            s2+=x
        if abs(int(n)-int(s1))<=abs(int(n)-int(s2)):
            return s1
        return s2



A=Solution()
print(A.nearestPalindromic("83"))