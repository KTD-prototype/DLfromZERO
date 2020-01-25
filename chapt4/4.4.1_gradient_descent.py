# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)  # new matrix with same shape as x

    for idx in range(x.size):
        tmp_val = x[idx]
        # calculate f(x+h)
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        # calculate f(x-h)
        x[idx] = float(tmp_val) - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # recover the value as initial state

    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        return grad


def function_1(x):
    return 0.01 * x**2 + 0.1 * x


def function_2(x):
    return x[0]**2 + x[1]**2


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d * x
    return lambda t: d * t + y


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x



if __name__ == '__main__':
    init_x = np.array([-3.0, 4.0])
    result = gradient_descent(function_2, init_x, lr=1e-10, step_num=100)
    print(result)

    # x0 = np.arange(-2, 2.5, 0.25)
    # x1 = np.arange(-2, 2.5, 0.25)
    # X, Y = np.meshgrid(x0, x1)
    #
    # X = X.flatten()
    # Y = Y.flatten()
    #
    # grad = numerical_gradient(function_2, np.array([X, Y]).T).T
    #
    # plt.figure()
    # plt.quiver(X, Y, -grad[0], -grad[1], angles="xy", color="#666666")
    # plt.xlim([-2, 2])
    # plt.ylim([-2, 2])
    # plt.xlabel('x0')
    # plt.ylabel('x1')
    # plt.grid()
    # plt.draw()
    # plt.show()
