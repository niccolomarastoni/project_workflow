def successor(n):
    return n + 1

def is_prime(n):
    for i in range(2, n // 2 + 1 ):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    for i in range(20):
        print(i, ' is prime? ', is_prime(i))
