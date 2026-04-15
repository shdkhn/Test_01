import math

def is_prime(n):
    if n <= 1:
        return False
    # Check from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example Usage
num = 29
print(f"{num} is prime? {is_prime(num)}")

