x=8
alpha=0.01

for i in range(1, 10):
    dx = (2*x) - 6
    xNext = x - (alpha * dx)
    x = xNext

    print(dx, xNext, x)

#end for


print(x)

# def f(x):
#     return (x**2) - (6*x) + 5
#
# import numpy as np
# v = np.array(range(-5, 10))
#
# print(f(v))