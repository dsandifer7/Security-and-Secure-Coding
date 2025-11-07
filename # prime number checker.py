# prime number checker

def prime_in_range(start, end):
    primes = []
    for i in range(start, end + 1):
        factors = []
        if end % i == 0:
            factors.append(i)
        if len(factors) == 2:
            primes.append(i)
    print(primes)
    
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
prime_in_range(start, end)