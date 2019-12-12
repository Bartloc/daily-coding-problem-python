from functools import lru_cache

@lru_cache()
def coins_optimal(coins):
    def F(i=0,j=0):   
        if j==i:
            return coins[j]
        if j==i+1:
            return max(coins[j],coins[i])
        return max((coins[i]+min(F(i+2,j),F(i+1,j-1))),\
                   coins[j]+min(F(i+1,j-1),F(i,j-2)))
    i=0
    j=len(coins)-1
    return F(i,j)

assert coins_optimal((1,2,1000,2,100))==104
