import numpy as np
import sys
import os
sys.path.append(os.pardir)
from master.common.gradient import numerical_gradient
from master.common.functions import softmax, cross_entropy_error
import simpleNet as simpleNet


def f(W):
    return net.loss(x, t)

net = simpleNet.simpleNet()
print(net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

print(np.argmax(p))

t = np.array([0, 0, 1]) # correct labels
print(net.loss(x, t))

dW = numerical_gradient(f, net.W)
print(dW)
