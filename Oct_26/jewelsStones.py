class Solution1(object):
    def numJewelsInStones(self, jewels, stones):

        res=0
        for i in jewels:
            for j in stones:
                if i in j:
                    res+=1
        return res

a = Solution1()
jewels = "aA"
stones = "aAAbbbb"
print(a.numJewelsInStones(jewels, stones))
