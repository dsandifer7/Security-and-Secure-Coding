def primelist(a, b):
    primes = []
    for i in range(a, b+1):
        factors = []
        for each in range(1,i+1):
            if i % each == 0:
                factors.append(each)
        if len(factors) == 2:
            primes.append(i)
    return primes
number1 = int(input("Enter the lower limit: "))
number2 = int(input("Enter the upper limit: "))
print(primelist(number1,number2))