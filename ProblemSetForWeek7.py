##First Task
def pow3(x, n):
    r = 1
    while n:
        if n % 2 == 1:
            r *= x
            n -= 1
        x *= x
        n /= 2
    return r

## Second Task
def loc_peaks(arr,i,j):
    middle = math.floor(((i+j)/2))
    if (arr[middle] > arr[middle-1] and arr[middle] > arr[middle+1]): 
        return arr[middle]
    elif arr[middle] < arr[middle-1]:
        return loc_peaks(arr,i,middle-1)
    elif arr[middle] < arr[middle+1]:
        return loc_peaks(arr,middle+1,j)
    
    
    
## Third Task    
def findMin(arr):
    minNum = 100000000
    minNumIndex = 0
    for i in range(len(arr)):
        if minNum > arr[i]:
            minNum = arr[i]
            minNumIndex = i
    return minNumIndex
def findShiftK(arr):
    return findMin(arr)
