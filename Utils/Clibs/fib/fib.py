from ctypes import cdll
lib = cdll.LoadLibrary('C:/Users/ketongu/PycharmProjects/NNWtest/Utils/Clibs/fib/libfib.so')
from time import time
from numba import njit


@njit(cache=True)
def numba_fib(n):
    if n <= 1:
        return 1
    else:
        return numba_fib(n - 1) + numba_fib(n - 2)


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class Fib(object):
    def __init__(self):
        self.obj = lib.Fib_new()

    def bar(self):
        lib.Fib_bar(self.obj)

    def fib(self, n):
        return lib.Fib_fib(self.obj, n)

    def speedDiff(self, n):
        print("\nDemonstrates speed difference between c++, clear python and python with numba via calculating n's Fibonachy number")
        t0 = time()
        res = self.fib(n)
        t1 = float(time() - t0)
        print("c++", '%.4f' % t1, "s")
        t0 = time()
        res = fib(n)
        t2 = float(time() - t0)
        print("python", '%.4f' % t2, "s")
        t0 = time()
        res = numba_fib(n)
        t3 = float(time() - t0)
        print("numba", '%.4f' % t3, "s")
        print(res, '\n python/c %.2f \n' % float(t2 / t1), 'numba/c %.2f \n' % float(t3 / t1),
              'python/numba %2.f \n' % float(t2 / t3))
