# coding: utf-8

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backard(self, dout):
        dx = dout * self.y # flip x and y
        dy = dout * self.x

        return dx, dy
