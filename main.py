# v1.1.1

from Internals import *
from App import Application
import _thread
from time import sleep

def main():
    def run(portIn: str):
        global port
        port = portIn
        _thread.start_new_thread(arduinoLoop,())

    def arduinoLoop():
        arduino = Hardware(port=port)
        while True:
            # mode = 1
            # temp = manager.getTemp()
            # arduino.invoke(mode, temp)
            # sleep(1)

            mode = 2
            (cpu, ram) = manager.get()
            if cpu > 100: cpu = 100
            if ram > 100: ram = 100
            arduino.invoke(mode, cpu)

            mode = 3
            sleep(1)
            arduino.invoke(mode, ram)

    manager = System_info_manager(interval=1)
    devices = Hardware.find()
    app = Application(devices)
    app.callback = lambda port: run(port)
    app.start()

if __name__ == '__main__':
    main()