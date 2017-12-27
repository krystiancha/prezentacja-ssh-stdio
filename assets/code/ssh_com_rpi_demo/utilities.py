from collections import UserList
from gmpy2 import xmpz, div, mul, add
from io import StringIO


class FixedSizeList(UserList):
    def __init__(self, source_list=None):
        super().__init__()
        if source_list is None:
            source_list = []
        self.data = source_list

    def push(self, element):
        self.data = [element] + self.data[:-1]


def pidigits(n):
    f = StringIO()

    k = 1

    n1 = xmpz(4)
    n2 = xmpz(3)
    d = xmpz(1)
    f10 = xmpz(10)
    n10 = xmpz(-10)

    i = 0
    while True:
        # digit
        u = int(div(n1,d))
        v = int(div(n2,d))
        if u == v:
            f.write(chr(48+u))
            i += 1

            if i == n:
                break

            # extract
            u = mul(d, mul(n10, u))
            n1 = mul(n1, f10)
            n1 = add(n1, u)
            n2 = mul(n2, f10)
            n2 = add(n2, u)
        else:
            # produce
            k2 = k << 1
            u = mul(n1, k2 - 1)
            v = add(n2, n2)
            w = mul(n1, k - 1)
            n1 = add(u, v)
            u = mul(n2, k + 2)
            n2 = add(w, u)
            d = mul(d, k2 + 1)
            k += 1

    f.write("%s" % (' ' * (10 - (i % 10))))
    return f.getvalue()
