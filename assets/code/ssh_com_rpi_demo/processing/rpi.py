from ast import literal_eval
from sys import stdin, stderr
from timeit import timeit

from math import exp

from processing.pidigits import pidigits


def pidigits_local(n):
    return pidigits(n)


def pidigits_remote(n):
    print({'pidigits': n})
    data = literal_eval(stdin.readline().strip())
    return data['pidigits']


NUMBER = 5

local_times = []
remote_times = []

for n in [10 ** i for i in range(0, 4)]:
    local_times.append(timeit(lambda: pidigits_local(n), number=NUMBER) / NUMBER)
    remote_times.append(timeit(lambda: pidigits_remote(n), number=NUMBER) / NUMBER)

print({'results': {'local': local_times, 'remote': remote_times}})
