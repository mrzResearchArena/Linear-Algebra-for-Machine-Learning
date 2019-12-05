# f(x)  = (x**2) - (6*x) + 5
# f'(x) = (2*x) - 6

x=8        # random start
alpha=0.01 # learning rate

for i in range(1, 10): # epoch
    dx = (2*x) - 6
    x = x - (alpha * dx)
    
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

# Resources:
# [1] https://abdalimran.github.io/2018-05-18/Intuition-of-Gradient-Descent-for-Machine-Learning
