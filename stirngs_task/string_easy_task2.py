class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        y=0
        x=0
        c_x=0
        c_y=0
        while x<len(name):
            ini_x = x
            ini_y=y
            while x<len(name) and name[x] == name[ini_x]:
                x += 1
            if typed[y]!=name[ini_x] or c_x>c_y:
                return False
            while y<len(typed) and typed[y]==name[ini_x]:
                y+=1
            c_x=x-ini_x
            c_y=y-ini_y
        if name[len(name)-1]!=typed[len(typed)-1]:
            return False
        return True

S=Solution()
print(S.isLongPressedName("saeed","ssaaedd"))