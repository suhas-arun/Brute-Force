import matplotlib.pyplot as plt

x_values = []
y_values = []

with open("data.txt", "r") as f:
    numbers = f.read().split()
    for i, number in enumerate(numbers):
        x_values.append(i)
        y_values.append(number)

    plt.plot(x_values, y_values)
    plt.show()
