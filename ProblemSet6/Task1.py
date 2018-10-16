def minCoins(C,V): # C - sortedArr ;; V - money in coins
    res = 0
    j = len(C) -1
    minNum = 0
    while(res != V):
        if(C[j]+res <= V):
            res += C[j]
            minNum+=1
        elif(C[j]+res > V):
            j-=1
        if j < 0:
            return "Impossible"
    return minNum
C = [10,70,120]
V = 140
print minCoins(C,V)
