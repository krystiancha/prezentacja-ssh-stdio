from ast import literal_eval
from subprocess import Popen, PIPE
from threading import Thread

from math import exp
from matplotlib import pyplot as plt
from numpy import logspace
from scipy.interpolate import spline, interp1d

from processing.pidigits import pidigits


class Master:
    def __init__(self, slave_stdout, slave_stdin):
        self.slave_stdout = slave_stdout
        self.slave_stdin = slave_stdin

        self.process_stdout_thread = Thread(target=self._process_stdout, daemon=False)
        self.process_stdout_thread.start()

        self.results = None

    def _process_stdout(self):
        for line in self.slave_stdout:
            data = literal_eval(line)

            if 'pidigits' in data:
                n = data['pidigits']
                self.slave_stdin.write(str({'pidigits': pidigits(int(n))}) + '\n')
                print(n)

            if 'results' in data:
                self.results = data['results']
                print('done')


def plot():
    x = [10 ** i for i in range(0, 4)]
    xnew = logspace(0, 3, num=50, endpoint=True)
    plt.loglog(xnew, interp1d(x, m.results['local'])(xnew), label='Local')
    plt.loglog(xnew, interp1d(x, m.results['remote'])(xnew), label='Remote (on a PC through SSH)')
    plt.title('Calculating n digits of pi on a Raspberry Pi')
    plt.xlabel('n')
    plt.ylabel('time [s]')
    plt.legend(loc='upper left')
    plt.show()


slave = Popen(
    ['ssh', 'protecto@192.168.8.110', 'cd ssh_com_rpi_demo && python3 -u -m processing.rpi'],
    bufsize=1,
    stdin=PIPE,
    stdout=PIPE,
    shell=False,
    universal_newlines=True,
)

m = Master(
    slave_stdin=slave.stdin,
    slave_stdout=slave.stdout,
)
