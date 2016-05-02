def amicableNumber():
    totalSum = 0
    def sumOfDivisors(numb):
        sumD = 0
        for d in range(numb/2):
            d += 1
            if numb%d ==0:
                sumD += d
        return sumD
    for i in range(10000-1):
        i += 1
        if i == sumOfDivisors(i):
            continue
        if i == sumOfDivisors(sumOfDivisors(i)):
            totalSum += i    
    print totalSum
    
amicableNumber()
