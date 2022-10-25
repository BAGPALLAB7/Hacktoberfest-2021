'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143
'''

n = 600851475143
primes = [1]

for i in range(2,n):

    if n % i == 0:
        primes.append(i)
        while n%i == 0:
         n = n/i


print(primes)
print(f"The largest prime factor of the number {n} is {max(primes)}")
