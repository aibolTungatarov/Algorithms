import time
class AidanaSequence(object):
    def recursion_way(self, n):
        if n == 0 or n == 1 or n == 2:
            return 1
        return self.recursion_way(n-1) + self.recursion_way(n-2) + self.recursion_way(n-3)
    def storing_elements(self, n):
        F = []
        for i in range(n+1):
            F.append(0)
        F[0] = 1
        F[1] = 1
        F[2] = 1
        for i in range(3,n+1):
            F[i] = F[i-1] + F[i-2] + F[i-3]
        return F[n]
    def rec(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.rec(n-1)+self.rec(n-2)
    def bruteForceGCD(self,a,b):   # 2(a+b)
        best = 1
        for i in range(1,a+b):
            if a%i == 0 and b%i == 0:
                best = i
        return best
    def gcd(self, a, b): #Euclid's
        if b > a:
            return self.gcd(b, a)
        if a%b == 0:
            return b
        return self.gcd(b, a % b)
aidanaSeq = AidanaSequence()
print("With recursion " , aidanaSeq.recursion_way(10))
print("With storing elements ", aidanaSeq.storing_elements(20))

start_time = time.time()
print(aidanaSeq.gcd(340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
elapsed_time = time.time() - start_time
print ("With Euclid's alghorithm  " + str(elapsed_time))

start_time = time.time()
print(aidanaSeq.bruteForceGCD(7000000,1000000))
elapsed_time = time.time() - start_time
print ("With bruteforce gcd " + str(elapsed_time))



#log(a*b)

