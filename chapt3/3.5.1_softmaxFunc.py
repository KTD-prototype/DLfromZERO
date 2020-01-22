import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)  # exponential function
print(exp_a)

sum_exp_a = np.sum(exp_a)  # sum of the exponential functions
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)
print("")

a = np.array([1010, 1000, 990])
# np.exp(a) / np.sum(np.exp(a)) #calculation of softmax func

c = np.max(a)  # maximum of the components of a : 1010
d = a - c
print(d)

ans = np.exp(a - c) / np.sum(np.exp(a - c))
print(ans)


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # subtract c in case of overflow when components of a is large
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
