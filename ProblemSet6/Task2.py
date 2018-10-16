def computeT(F): # F - array of sizes
    F.sort()
    T = 0
    sum = 0
    for i in range(len(F)):
        sum += sumOf(F,i)
    return sum/len(F)
def sumOf(arr,to):
    sum = 0
    for i in range(to+1):
        sum+=arr[i]
    return sum
print computeT([500,100,300])

