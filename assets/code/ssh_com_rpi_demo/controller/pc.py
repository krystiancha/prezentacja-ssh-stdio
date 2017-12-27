from ast import literal_eval
from subprocess import Popen, PIPE
from threading import Thread

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import CheckButtons

from utilities import FixedSizeList


class PC:
    PARAM_NAMES = ['r', 'g', 'b']

    def __init__(self, rpi_stdout, rpi_stdin):
        self.rpi_stdout = rpi_stdout
        self.rpi_stdin = rpi_stdin

        self.samples_visible = 10
        self.x_head = 0

        self.xdata = FixedSizeList(
            [None for _ in range(self.samples_visible)]
        )
        self.ydata = FixedSizeList(
            [None for _ in range(self.samples_visible)]
        )

        self._init_gui()

        self.process_input_thread = Thread(
            target=self._process_input,
            daemon=False,
        )
        self.process_input_thread.start()

    def _init_gui(self):
        self.fig = plt.figure()

        gs = GridSpec(1, 2)

        self.scope_ax = self.fig.add_subplot(gs[0, 0])
        self.scope_ax.set_ylim(20, 30)
        self.scope_ax.get_xaxis().set_visible(False)
        self.scope = self.scope_ax.plot([0, 1, 2], [0.5, 0.5, 0.5])[0]
        self.animation = FuncAnimation(self.fig, self._update_scope, blit=True, interval=1)

        self.checkbuttons_ax = self.fig.add_subplot(gs[0, 1])
        self.checkbuttons = CheckButtons(self.checkbuttons_ax, self.PARAM_NAMES,
                                         [False for _ in range(len(self.PARAM_NAMES))])
        self.checkbuttons.on_clicked(lambda key: self.rpi_stdin.write(
            str({'rgb': {key: self.checkbuttons.get_status()[self.PARAM_NAMES.index(key)]}}) + '\n'))

    def _process_input(self):
        for line in self.rpi_stdout:
            data = literal_eval(line)

            if 'temperature' in data:
                self.x_head += 1
                self.xdata.push(self.x_head)
                self.ydata.push(data['temperature'])

    def _update_scope(self, frame=None):
        self.scope.set_data(self.xdata, self.ydata)
        self.scope_ax.set_xlim(
            self.x_head - self.samples_visible + 1,
            self.x_head,
        )
        return self.scope,


rpi = Popen(
    [
        'ssh',
        'protecto@192.168.8.110',
        'cd ssh_com_rpi_demo && python3 -u -m controller.rpi'
    ],
    bufsize=1,
    stdin=PIPE,
    stdout=PIPE,
    shell=False,
    universal_newlines=True,
)

pc = PC(
    rpi_stdout=rpi.stdout,
    rpi_stdin=rpi.stdin,
)

plt.show()
