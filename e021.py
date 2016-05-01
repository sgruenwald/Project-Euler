def amicableNumber():
    totalSum = 0
    def sumOfDivisors(numb):
        sumD = 0
        for d in range(numb/2):
            d = d+1
            if numb%d ==0:
                sumD = sumD + d
        return sumD
    for i in range(10000-1):
        i = i+1
        if i == sumOfDivisors(i):
            continue
        if i == sumOfDivisors(sumOfDivisors(i)):
            print i
            totalSum = totalSum + i    
    print "Evaluate the sum of all the amicable numbers under 10000:",totalSum
    
amicableNumber()