class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dist = 1
        lengt = len(seats)
        for x in range(lengt):
            t_dist = 1
            if seats[0] == 0 and x == 0:
                x+=1
                while x<lengt and seats[x] != 1:
                    t_dist += 1
                    x += 1

            elif seats[x] == 1:
                x += 1
                while x<lengt and seats[x] != 1:
                    x += 1
                    t_dist += 1

                if x==lengt and seats[x-1]!=1:
                    t_dist-=1
                elif t_dist % 2 == 0:
                    t_dist = t_dist / 2
                else:
                    t_dist = (t_dist // 2)
            t_dist=int(t_dist)
            if t_dist > dist:
                dist = t_dist
        return dist



A=Solution()
print(A.maxDistToClosest([0,1]))