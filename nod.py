def gcd(a, b):
    a_divisors = [a // i for i in range(1, a+1) if a % i == 0]
    b_divisors = [b // i for i in range(1, b+1) if b % i == 0]
    for divisor in min(a_divisors, b_divisors):
        if divisor in max(a_divisors, b_divisors):
            return divisor

print(gcd(48, 36))
