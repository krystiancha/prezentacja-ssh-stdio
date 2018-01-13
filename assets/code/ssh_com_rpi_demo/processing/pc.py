from ast import literal_eval
from subprocess import Popen, PIPE
from threading import Thread

from matplotlib import pyplot as plt
from numpy import logspace
from scipy.interpolate import interp1d

from config import SSH_USER_HOSTNAME
from utilities import pidigits


class PC:
    def __init__(self, rpi_stdout, rpi_stdin):
        self.rpi_stdout = rpi_stdout
        self.rpi_stdin = rpi_stdin

        self.process_stdout_thread = Thread(target=self._process_input, daemon=False)
        self.process_stdout_thread.start()

        self.results = None

    def _process_input(self):
        for line in self.rpi_stdout:
            data = literal_eval(line)

            if 'pidigits' in data:
                n = data['pidigits']
                self.rpi_stdin.write(str({'pidigits': pidigits(int(n))}) + '\n')

            if 'results' in data:
                self.results = data['results']


def plot():
    x = [10 ** i for i in range(0, 4)]
    xnew = logspace(0, 3, num=50, endpoint=True)
    plt.loglog(xnew, interp1d(x, m.results['local'])(xnew), label='bezpośrednio na Raspberry Pi')
    plt.loglog(xnew, interp1d(x, m.results['remote'])(xnew), label='RPi zleca obliczenia szybszemu komputerowi')
    plt.title('Obliczanie n cyfr rozwinięcia dziesiętnego liczby Pi')
    plt.xlabel('n')
    plt.ylabel('czas [s]')
    plt.legend(loc='upper left')
    plt.show()


rpi = Popen(
    [
        'ssh',
        SSH_USER_HOSTNAME,  # robot@192.168.123.101
        'cd ssh_com_rpi_demo && python3 -u -m processing.rpi'
    ],
    bufsize=1,
    stdin=PIPE,
    stdout=PIPE,
    shell=False,
    universal_newlines=True,
)

m = PC(
    rpi_stdin=rpi.stdin,
    rpi_stdout=rpi.stdout,
)
