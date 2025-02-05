"""Factor finder"""
n = int(input("Enter a positive integer: "))

factors = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        factors.append(i)
        other_factor = int(n / i)
        # check if the numbers are equal to avoid duplicates with square numbers
        if i != other_factor:
            factors.append(other_factor)

str_factors = ", ".join(list(map(str, sorted(factors))))
print(f"\n{n} has {len(factors)} factors:\n\n{str_factors}")
