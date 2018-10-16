import math
def numberToD(n):
    if n%10 == n:
        return str(n)
    print str(n%10)
    return numberToD(int(math.floor(n/10)))

#numberToD(1321321312000238789


def factorial(a):
    if a==1:
        return 1
    else:
        return factorial(a-1)*a
print (factorial(5))
s = "aibol"
n = len(s)
print s[0:len(s)-1]

def listt(a):
    if len(a) == 1:
        return a
    print (a[len(a)-1])
    return listt(a[0:len(a)-1])
print listt('isla')



