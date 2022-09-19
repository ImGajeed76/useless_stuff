from useless.useless_number import *


class Array:
    def __init__(self, *args):
        self.array = list(args)

    def __getitem__(self, item: int):
        return self.array[item]

    def __setitem__(self, key: int, value):
        self.array[key] = value
        return self

    def __str__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

    def index_of(self, value):
        for i in range(len(self.array)):
            if self.array[i] == value:
                return i
        return None

    def append(self, value):
        self.array.append(value)
        return self

    def push(self, value):
        self.array = [value] + self.array
        return self

    def pop(self):
        self.array.pop()
        return self

    def shift(self):
        self.array = self.array[1:]
        return self

    def combination(self, n: int):
        combination = number_to_base(n, len(self))
        print(combination)
        result = []
        for c in combination:
            result.append(self.array[c])
        return [result]

    def combinations(self, limit: int = None):
        result = []
        for i in range(len(self) ** len(self)):
            if limit and i >= limit:
                break
            result += self.combination(i)
        return result
