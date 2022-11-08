from numba import jit, njit, cuda
from timeit import default_timer as timer  
import numpy as np

@jit(target_backend='cuda')
def func(start, end):
    def innerCheckForPrime(number) -> bool:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True
    primes = []
    for i in range(start, end):
        if innerCheckForPrime(i):
            primes.append(i)
    print('primes:', len(primes))

@jit(target_backend='CPU')
def func2(start, end):
    def innerCheckForPrime(number) -> bool:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True
    primes = []
    for i in range(start, end):
        if innerCheckForPrime(i):
            primes.append(i)
    print('primes:', len(primes))

@jit(target_backend='CPU')
def func3(start, end):  
    primes = []
    for i in range(start, end):
        if CheckForPrime(i):
            primes.append(i)

    print('primes:', len(primes))


def CheckForPrime(number) -> bool:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True

@jit
def numpy_test():
    x = np.array([1,2,3,4])
    y = np.array([4,3,2,1])
    print(np.add(x, y))
    return x + y


if __name__ == '__main__':
    print('Running')

    print(numpy_test())
    # iterations = 30000

    # start = timer()
    # func(1, iterations)
    # print(f"With GPU: {timer()-start}")

    # start = timer()
    # func2(1, iterations)
    # print(f"With CPU: {timer()-start}")

    # start = timer()
    # func3(1, iterations)
    # print(f"Standard: {timer()-start}")