import serial
import psutil
import serial.tools.list_ports
from time import sleep

class Hardware:
    s = serial.Serial()
    def __init__(self, port: str):
        self.s.port = port
        self.s.baudrate = 115200
        self.s.open()

    def invoke(self, mode: int, data: int):
        cmd = 'G' + str(mode) + ' ' + str(data)
        self.s.write(cmd.encode())

    @classmethod
    def find(cls) -> list:
        availables = ['Please select from below:']
        for device in serial.tools.list_ports.comports():
            availables.append(device.device)
        print(availables)
        return availables
        # print(len(psutil.sensors_temperatures()))


class System_info_manager:
    interval = 0.0
    def __init__(self, interval: float = 1.0):
        self.interval = interval

    def get(self) -> (int, int):
        # net_0s = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent
        cpu = int(psutil.cpu_percent(self.interval))
        # net_change = (psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent - net_0s)
        # net = int(net_change / self.interval / 1024 / 1024 / 10 * 255)
        ram = int(psutil.virtual_memory().percent)
        # no * 2.25
        return cpu, ram

    def getTemp(self) -> int:
        return 50
