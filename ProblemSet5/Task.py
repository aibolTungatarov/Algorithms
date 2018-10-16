import random
class Task:
    def __init__(self):
        pass

    #################################
    #################################
    def sort(self, arrA):
        n = len(arrA)
        arrB  = [None] * n
        j = 0
        while(n >= 1):
            min = 1000000
            for i in range(n):
                if min > arrA[i]:
                    min = arrA[i]
            arrB[j] = min
            arrA.remove(min)
            n-=1
            j+=1
        return arrB
    #################################
    #################################
    def running_time_of_bruteforce(self):
        return "Running time is O(n^2)"
    #################################
    #################################
    def max_sum(self, arr):
        n = len(arr)
        sum = 0
        for i in range(n):
            if arr[i] > 0:
                sum += arr[i]
        return sum

    #################################
    #################################
    # running time is T(n) = n^2 + 2n
     ###### stupid algo that takes 3 argument n, a , b and randomly creates array of size n that contains values from a to b and sorts them
    def stupid_algorithm(self, n, a, b):
        arr = [None]*n
        for i in range(n):
            randInt = random.randint(a, b)
            arr[i] = randInt
        arr = self.sort(arr)
        return arr
    def sumIt(self, arr):
        sum = 0
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                sum += arr[i][j]
        return sum
    #O(2^n)
    def rec(self,arr):
        if not arr:
            return [[]]
        head, tail = arr[:1], arr[1:]
        res = self.rec(tail)
        return res + [head + s for s in res]

task = Task()
task.stupid_algorithm(10, -10, 10)
arr = [1,2,3,4,5,3]
print (task.powset2(arr,0))
