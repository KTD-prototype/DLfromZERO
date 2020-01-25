import numpy as np
import sys
import os
sys.path.append(os.pardir)
from master.common.gradient import numerical_gradient
from master.common.functions import softmax, cross_entropy_error

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # initialize with gauss distribution

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss
