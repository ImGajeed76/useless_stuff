import math

import numpy as np


class Matrix:
    mat = np.zeros((1, 1))
    shape = (1, 1)

    def __init__(self, args: tuple[int, int] or list[list]):
        if type(args) == tuple:
            self.mat = np.zeros((args[1], args[0]))
            self.shape = (args[1], args[0])
        elif type(args) == list:
            self.mat = np.array(args)
            self.shape = self.mat.shape

    def fill_ones(self):
        self.mat = np.ones(self.shape)
        return self

    def fill_zeros(self):
        self.mat = np.zeros(self.shape)
        return self

    def fill_default(self):
        self.mat = np.zeros(self.shape)

        for x in range(self.shape[1]):
            try:
                self[x, x] = 1
            except:
                pass

        return self

    def get(self, x, y):
        return self.mat[y, x]

    def set(self, x, y, val):
        self.mat[y, x] = val
        return self

    def __getitem__(self, item):
        return self.mat[(item[1], item[0])]

    def __setitem__(self, key, value):
        self.mat[(key[1], key[0])] = value
        return self

    def __str__(self):
        return str(self.mat)

    def __mul__(self, other):
        self.mat = np.matmul(self.mat, other.mat)
        return self

    def __add__(self, other):
        self.mat = np.add(self.mat, other.mat)
        return self

    def __sub__(self, other):
        self.mat = np.subtract(self.mat, other.mat)
        return self

    def generate_perspective(self, fov: float = 90, far: float = 1000, near: float = 0.01):
        self.shape = (4, 4)
        self.fill_default()
        s = 1 / math.tan((fov / 2) * (math.pi / 180))

        self[0, 0] = s
        self[1, 1] = s
        self[3, 2] = -1
        self[2, 2] = -(far / (far - near))
        self[2, 3] = -((far * near) / (far - near))

        return self

    def get_xyzw(self):
        coords = np.matmul(self.mat, np.array([[1], [1], [1], [1]]))
        return coords[0, 0], coords[1, 0], coords[2, 0], coords[3, 0]
