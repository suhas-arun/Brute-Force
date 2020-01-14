"""Calculates 2^n with bit shifting"""
N = int(input("Enter number: "))
if N == 0:
    print(1)
else:
    print(2 << N - 1)
