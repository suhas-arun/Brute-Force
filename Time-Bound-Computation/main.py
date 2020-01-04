"""
Comparing efficiency of matrix multiplication using Python, Numpy and Numba.jit
"""
import time
import matplotlib.pyplot as plt
import numpy as np
from numba import jit


def python_multiply(a, b, n):
    """performs matrix mutliplication without using numpy"""
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


@jit(nopython=True)
def numba_multiply(a, b, n):
    """performs matrix multiplication using the numba compiler"""
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


py_data: dict = {"n": [], "time": []}
numba_data: dict = {"n": [], "time": []}
numpy_data: dict = {"n": [], "time": []}

for n in range(100, 1000, 100):
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)

    # multiplication using just python
    py_start_time = time.time()
    py_result = python_multiply(a, b, n)
    py_end_time = time.time()

    py_data["n"].append(n)
    py_data["time"].append(py_end_time - py_start_time)

    # multiplication using numba.jit
    numba_start_time = time.time()
    numba_result = numba_multiply(a, b, n)
    numba_end_time = time.time()

    numba_data["n"].append(n)
    numba_data["time"].append(numba_end_time - numba_start_time)

    # multiplication using numpy
    numpy_start_time = time.time()
    numpy_result = np.dot(a, b)
    numpy_end_time = time.time()

    numpy_data["n"].append(n)
    numpy_data["time"].append(numpy_end_time - numpy_start_time)


plt.plot("n", "time", data=py_data, label="Python")
plt.plot("n", "time", data=numba_data, label="Numba")
plt.plot("n", "time", data=numpy_data, label="Numpy")

plt.legend()

plt.xlabel("n")
plt.ylabel("time")

plt.savefig("Time-Bound-Computation/graph.png")
plt.show()
