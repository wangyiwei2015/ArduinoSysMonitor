from Internals import *
from gui import Application, ErrorWindow
import _thread

# arduino = Hardware(port='/dev/tty.usbmodem14201')

def  main():
    def run(portIn: str):
        global port
        port = portIn
        _thread.start_new_thread(arduinoLoop,(None,None))

    def arduinoLoop(_,nothing):
        arduino = Hardware(port=port)
        while True:
            mode = 1
            temp = manager.getTemp()
            sleep(1)
            arduino.invoke(mode, temp)

            mode = 2
            (cpu, ram) = manager.get()
            if cpu > 100: cpu = 100
            if ram > 100: ram = 100
            arduino.invoke(mode, cpu)

            mode = 3
            sleep(1)
            arduino.invoke(mode, ram)

    manager = System_info_manager(interval=1.0)
    shouldContinue = False
    try:
        devices = Hardware.find()
        shouldContinue = True
    except:
        _ = ErrorWindow()
        return -1

    if shouldContinue:
        if(len(devices) < 2):
            print('No available device.')
            _ = ErrorWindow()
            shouldContinue = False

        if shouldContinue:
            print('start')
            app = Application(devices)
            app.callback = lambda port: run(port)
            app.start()

if __name__ == '__main__':
    return_value = main()
    print('Finished with return', return_value)

'''
    print('\n')
    i = 0
    for device in devices:
        print('[%d]' % (i), device)
        i += 1
    print('\n')
    sel = int(input('> '))
    if(sel > 0 and sel < i):
        i = sel
    else:
        print('Invalid.')
        return -2
'''