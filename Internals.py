import serial
import psutil
import serial.tools.list_ports

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
        availables = ["请选择设备"]
        for device in serial.tools.list_ports.comports():
            availables.append(device.device)
        return availables

class System_info_manager:
    interval = 0.0
    def __init__(self, interval: float = 1.0):
        self.interval = interval

    def get(self) -> (int, int):
        cpu = int(psutil.cpu_percent(self.interval))
        ram = int(psutil.virtual_memory().percent)
        return cpu, ram

    def getTemp(self) -> int:
        return 50
