from ast import literal_eval
from sys import stdin
from threading import Thread

from RPi import GPIO


class RPi:
    def __init__(self, pins, w1_slave):

        self.pins = pins
        self.w1_slave = w1_slave

        self.rgb = {key: False for key in self.pins.keys()}

        GPIO.setup(list(self.pins.values()), GPIO.OUT)
        GPIO.output(list(self.pins.values()), list(self.rgb.values()))

        self.process_input_thread = Thread(
            target=self._process_input,
            daemon=False,
        )
        self.process_input_thread.start()

        self.output_temperature_thread = Thread(
            target=self._output_temperature,
            daemon=True,
        )
        self.output_temperature_thread.start()

    def _process_input(self):
        for line in stdin:
            data = literal_eval(line)

            if 'rgb' in data:
                self.rgb.update(data['rgb'])

            GPIO.output(list(self.pins.values()), list(self.rgb.values()))

        GPIO.cleanup()

    def _output_temperature(self):
        while True:
            with open(self.w1_slave, 'r') as f:
                lines = f.readlines()
                if lines[0].strip()[-3:] == 'YES':
                    temperature_str = lines[1].strip()[-5:]
                    print({'temperature': float(temperature_str[:2] + '.' + temperature_str[2:])})


GPIO.setmode(GPIO.BCM)

s = RPi(
    pins={
        'r': 17,
        'g': 27,
        'b': 22,
    },
    w1_slave='/sys/bus/w1/devices/28-00000514b25d/w1_slave',
)
