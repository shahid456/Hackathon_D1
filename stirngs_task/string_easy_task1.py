class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        upd_emails=[]
        for email in emails:
            temp=""
            temp1=""
            atr=email.find('@')
            temp=email[0:atr]
            x=0
            l=len(temp)
            while x<l:
                if temp[x]=='.':
                    temp=temp.replace('.','',1)
                if temp[x]=='+':
                    break
                x=x+1
            temp=temp[0:x]
            temp1=email[atr:len(email)]
            temp1=temp+temp1
            if temp1 in upd_emails:
                pass
            else:
                upd_emails.append(temp1)
        return len(upd_emails)
A=Solution()

print(A.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))