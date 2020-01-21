import sys, os
sys.path.append(os.pardir)
from master.dataset.mnist import load_mnist
from Functions.functions import sigmoid, softmax
import numpy as np
import pickle
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def get_data():
    # loadin data at first time will take several minutes
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = True, one_hot_label = False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network


# def softmax(a):
#     c = np.max(a)
#     exp_a = np.exp(a - c) # subtract c in case of overflow when components of a is large
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#     return y
#
#
# def sigmoid_function(x):
#     return 1 / (1 + np.exp(-x))


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x,t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y) # get an index with the highest probability
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy : " + str(float(accuracy_cnt) / len(x)))